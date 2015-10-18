---
title: Invited talks
---

# Invited talks
{:.no_toc}

* Table of contents
{:toc}

{% for talk in site.data.manualschedule.papers %}

## {{ talk[0] }}

Title
: *{{ talk[1].title | strip_newlines }}*

{% if talk[1].slides  %}
Slides
: [PDF](slides/{{ talk[1].slides }})
{% endif %}

Abstract
: {{ talk[1].abstract }}

Biography
: {{ talk[1].biography }}

{% endfor %}
