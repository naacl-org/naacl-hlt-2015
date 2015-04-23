import re

def cleanup(html):
    # remove everything until the first table, and everything after the last table
    start = html.index('<table>')
    end = html.rindex('</table>') + len('</table>')
    html = html[start:end]

    # add a "schedule" to the topmost table (used in the CSS):
    html = re.sub(r'<table>', '<table class="schedule">', html, count=1)

    # strip all lines
    html = "\n".join(line.strip() for line in html.splitlines())

    # remove comments
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    # html arguments must be quoted
    html = re.sub(r'<(\w+) (\w+)=(\w+)', r'<\1 \2="\3"', html)

    # remove links to PDF
    html = re.sub(r'<a href="[^"]+\.pdf">.*?</a>', '', html)

    # rename links to HTML abstracts
    html = re.sub(r'<a href="([^"]+\.html)"', r'<a href="accepted/\1"', html)

    # remove empty TD:s
    html = re.sub(r'<td>\s*</td>', '', html)

    return html


with open('accepted/accepted.html', 'r') as F:
    html = F.read()

with open('schedule.md', 'w') as F:
    print >>F, """---
title: NAACL-HLT 2015 Main Program Schedule
---
# NAACL HLT 2015 Program Schedule

""" + cleanup(html)

print "--> schedule.md"


with open('accepted/authorindex.html', 'r') as F:
    html = F.read()

with open('authorindex.md', 'w') as F:
    print >>F, """---
title: NAACL-HLT 2015 Author Index
---
# NAACL HLT 2015 Author Index

""" + cleanup(html)

print "--> authorindex.md"
