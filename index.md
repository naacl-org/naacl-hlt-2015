---
title: Welcome
---

# NAACL HLT 2015

Welcome to the 2015 Conference of the North American Chapter of the Association for Computational Linguistics – Human Language Technologies (NAACL HLT 2015), taking place May 31 to June 5 in Denver, Colorado, USA.

## [Deadlines](dates.html)

These are just the most important dates, there is another page that lists [all the important dates](dates.html).

- Long and short paper submissions: Dec 4, 2014
- Tutorial proposal submissions: Jan 9, 2015
- Demo submissions: Feb 13, 2015
- Student paper submissions: Mar 8, 2015 (extended from <del>Feb 25</del>)
- Workshop paper submissions: Feb 25, 2015 (many workshops have extended the deadline)

## [News](all-news.html)

{% for post in site.posts limit:5 %}

### {{ post.date | date: '%b %-d, %Y' }}: {{ post.title }}

{{ post.content }}

{% endfor %}

