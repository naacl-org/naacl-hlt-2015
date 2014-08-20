---
title: Welcome
---

Welcome to NAACL-HLT 2015 in Denver, Colorado!

# [News](all-news.html)

{% for post in site.posts limit:5 %}

## {{ post.date | date: '%b %-d, %Y' }}: {{ post.title }}

{{ post.content }}

{% endfor %}
