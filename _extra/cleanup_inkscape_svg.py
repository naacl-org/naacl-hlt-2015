
"""
Clean up SVG files saved by Inkscape. Call like this:

  python cleanup_inkscape_svg.py < naacl-hlt-2015-banner-original.svg > naacl-hlt-2015-banner.svg

NOTE: This is a hack and will definitely NOT work on all SVG files!
"""

import fileinput
from html.parser import HTMLParser

TAGS = {'svg': ['xmlns'],
        'g': ['transform'],
        'path': ['d', 'transform'],
        }

class SVGParser(HTMLParser):

    def handle_pi(self, data):
        print("<?%s>" % (data,))

    def handle_endtag(self, tag):
        if tag in TAGS:
            print("</%s>" % (tag,))

    def handle_starttag(self, tag, attrs, endtag=""):
        if tag in TAGS:
            print("<%s" % (tag,))
            wdt = hgt = 0
            for (att, val) in attrs:
                if att in TAGS[tag]:
                    print(' %s="%s"' % (att, val))
                elif att == 'width':
                    wdt = val
                elif att == 'height':
                    hgt = val
            if tag == 'svg' and wdt and hgt:
                print(' viewBox="0 0 %s %s"' % (wdt, hgt))
            print("%s>" % (endtag,))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs, endtag="/")

    def handle_comment(self, data):
        pass

    def handle_data(self, data):
        pass

    def handle_charref(self, name):
        raise NotImplementedError(name)

    def handle_decl(self, decl):
        raise NotImplementedError(decl)

    def handle_entityref(self, name):
        raise NotImplementedError(name)


def main():
    parser = SVGParser()
    for line in fileinput.input():
        parser.feed(line)
    parser.close()


if __name__ == '__main__':
    main()
