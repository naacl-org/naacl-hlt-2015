import re
header = """---
title: NAACL-HLT 2015 Main Program Schedule
---
"""
ispaper = re.compile('a href=\"\d+.pdf\"')
iscommented = re.compile('<\!--')
#print header
with open('accepted.html', 'r') as f:
    for line in f:
        line = line.strip()
        if ispaper.search(line):
            print '<!-- ', line, ' -->'
        else:
            print line
