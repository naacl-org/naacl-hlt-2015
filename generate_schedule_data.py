#!/usr/bin/env python3

"""
Usage: python3 generate_schedule_data.py > _data/schedule.yaml

A script that reads the Softconf-generated directories 'accepted'
and 'accepted-demos', and generates a YAML file with information
about papers, demos, authors and the schedule.
"""

import re
import glob
import sys
import datetime
import html
import yaml

SOFTCONF = 'softconf'

def read_paper_info(folder):
    papers = {}
    for filename in glob.glob('{}/{}/*[0-9].html'.format(SOFTCONF, folder)):
        id = filename[len(SOFTCONF) + len(folder) + 2 : -len('.html')]
        with open(filename) as F:
            htstr = html.unescape(F.read())
            htstr = re.sub(r'\s+', ' ', htstr)

        match = re.search(r'''
            <h4> \s* (?P<title> .+?) \s* </h4> \s*
            <em> \s* (?P<authors> .+?) \s* </em> \s* (<br>)?
            \s* (?P<affiliation> .*?) \s* <p> .*
            <blockquote> \s* (<p>)? \s* (?P<abstract> .+?) \s* (</p>)? \s* </blockquote>
        ''', htstr, flags=re.DOTALL | re.VERBOSE)
        if not match:
            match = re.search(r'''
                <h2> \s* (?P<title> .+?) \s* </h2> \s*
                <h3> \s* (?P<authors> .+?) \s* </h3> (?P<affiliation>) .*
                <h2> .* Abstract \s* </h2>
                \s* (?P<abstract> .+?) \s* <p> \s* <hr>
            ''', htstr, flags=re.DOTALL | re.VERBOSE)

        papers[id] = match.groupdict()
        abstract = papers[id]['abstract']
        abstract = '<p>' + re.sub(r'\s*<p>\s*', '</p><p>', abstract) + '</p>'
        papers[id]['abstract'] = abstract
        authors = re.sub(r'<sup>.*?</sup>', '', papers[id]['authors'])
        if authors != papers[id]['authors']:
            papers[id]['authors_with_affiliation'] = papers[id]['authors']
            papers[id]['authors'] = authors

    return papers


def read_authorindex(folder):
    with open('{}/{}/authorindex.html'.format(SOFTCONF, folder)) as F:
        htstr = html.unescape(F.read())

    index = []
    for tablerow in htstr.split('</tr>'):
        match = re.search(r'<big><big><big>(.+?)</big>', tablerow)
        if match:
            letter = match.group(1)
            if letter.isupper():
                index.append({'letter':letter, 'authors':[]})
            else:
                letter = None
            continue

        match = re.search(r'''
            <td> \s* <em> \s* (?P<author> .*?) \s* </em> \s*
            <br> \s* (?P<affiliation> .*?) \s* </td>
            ''', tablerow, flags=re.VERBOSE|re.DOTALL)
        if not match:
            continue

        entry = match.groupdict()
        entry['refs'] = re.findall(r'<a href="(\d+).html"', tablerow)
        if letter:
            index[-1]['authors'].append(entry)
        else:
            # The authorindex file errs for some surnames, such as "de Marneffe" and "van Schijndel"
            lastname = entry['author'].split()[-1]
            assert lastname[0].isupper(), entry
            for i in index:
                if lastname.startswith(i['letter']):
                    i['authors'].append(entry)
                    break
            else:
                print("Could not create author index for", entry, file=sys.stderr)

    return index


DATE, SESSION, EXTRA, TALK, SESSIONTALK = "date session extra talk sessiontalk".split()
ordertypes = {'*': DATE,
              '=': SESSION,
              '+': EXTRA,
              '!': TALK}

def read_order_file(papers):
    schedule = []
    with open('{}/order'.format(SOFTCONF)) as F:
        for line in F:
            line = re.sub(r'\s+', ' ', line.strip())
            ref, line = line.split(None, 1)
            cls = ordertypes.get(ref, TALK)
            if ref in ordertypes:
                ref = None

            if cls == DATE:
                date = line.split()[0]
                #date = line.strip()
                overview, talks = {}, {}
                schedule.append((date, overview, talks))
                sessiontime = None
                continue

            match = re.search(r'(\d\d:\d\d)--(\d\d:\d\d) (.+)$', line)
            if not match:
                print(line, file=sys.stderr)
                continue
            start, end, title = match.groups()
            time = start + '-' + end

            if cls == SESSION:
                if sessiontime != time:
                    sessiontime = time
                    assert sessiontime not in overview, line
                    overview[sessiontime] = {'class':cls, 'row':[]}
                else:
                    assert sessiontime in overview, line
                title = re.sub(r'^Session +', '', title, flags=re.IGNORECASE)
                overview[sessiontime]['row'].append([{'title':title}])

                match = re.search(r'^(Invited talk by .+?):', title, flags=re.IGNORECASE)
                if match:
                    # assert sessiontime not in talks, line
                    # overview[sessiontime]['class'] = SESSIONTALK
                    overview[sessiontime]['row'][-1][-1]['ref'] = match.group(1)

            else:
                thistalk = {}
                if sessiontime and timespan_within(time, sessiontime):
                    assert cls == TALK, line
                    talks.setdefault(sessiontime, {}).setdefault(time, [])
                    while len(overview[sessiontime]['row']) > len(talks[sessiontime][time]):
                        talks[sessiontime][time].append([])
                    talks[sessiontime][time][-1].append(thistalk)
                else:
                    if time in overview:
                        assert overview[time]['class'] == cls
                    else:
                        overview[time] = {'class':cls, 'row':[]}
                    overview[time]['row'].append([thistalk])
                    sessiontime = None

                if ref in papers:
                    thistalk['ref'] = ref

                else:
                    prefix = authors = None
                    match = re.search(r'^(?:Session .*?[-:] )?(.+?) %by (.+)$',
                                      title, flags=re.IGNORECASE)
                    if match:
                        title, authors = map(str.strip, match.groups())
                    if title.lower().startswith('invited talk by') or title.startswith('TACL-'):
                        prefix, title = map(str.strip, title.split(':', 1))
                        if prefix.lower().startswith('invited talk by'):
                            authors = None

                    if prefix in papers:
                        thistalk['ref'] = prefix
                    else:
                        if cls == TALK:
                            print('Talk not in papers database: {} "{}". {}'.format(
                                prefix or "", title, authors or ""
                                ), file=sys.stderr)
                        thistalk['title'] = title
                        if prefix:
                            thistalk['prefix'] = prefix
                        if authors:
                            thistalk['authors'] = authors

    new_schedule = []
    for date, overview, talks in schedule:
        year, month, day = map(int, date.split('/'))
        date = '{}-{:02d}-{:02d}'.format(year, month, day)

        today = []
        for sessiontime, session in sorted(overview.items()):
            session['time'] = sessiontime
            today.append(session)
            for time, talkrow in sorted(talks.get(sessiontime, {}).items()):
                cls = SESSIONTALK
                parent = 'session-{}'.format(sessiontime.replace(':',''))
                today.append({'time':time, 'class':cls, 'parent':parent, 'row':talkrow})
        new_schedule.append({'date':date, 'schedule':today})

    return new_schedule


def infer_talktypes(schedule, papers):
    talktypes = {}
    for today in schedule:
        for session in today['schedule']:
            if session['class'] != SESSIONTALK:
                parent_session = session
            else:
                for n, col in enumerate(session['row']):
                    sessiontitle = parent_session['row'][n][0]['title']
                    for item in col:
                        if item['ref'] in papers:
                            istacl = 'TACL-' in item['ref']
                            isposter = 'Poster' in sessiontitle
                            isshort = 'Short' in sessiontitle
                            paper = papers[item['ref']]
                            typ = 'tacl' if istacl else 'short' if isshort else 'long'
                            typ += 'posters' if isposter else 'talks'
                            talktypes.setdefault(typ, []).append(item['ref'])
    return talktypes


def get_timespan(time):
    return tuple(map(int, time.replace(':','').split('-')))


def timespan_within(t1, t2):
    s1, e1 = get_timespan(t1)
    s2, e2 = get_timespan(t2)
    return s2 <= s1 <= e1 <= e2


def printyaml(obj):
    # https://dpinte.wordpress.com/2008/10/31/pyaml-dump-option/
    print(yaml.dump(obj, default_style="'", default_flow_style=False, width=9999))


def main():
    demos = read_paper_info('accepted-demos')
    printyaml({'demos':demos})

    papers = read_paper_info('accepted-papers')
    printyaml({'papers':papers})

    authorindex = read_authorindex('accepted-papers')
    printyaml({'authorindex':authorindex})

    schedule = read_order_file(papers)
    printyaml({'schedule':schedule})

    talktypes = infer_talktypes(schedule, papers)
    printyaml({'talktypes':talktypes})


if __name__ == '__main__':
    main()
