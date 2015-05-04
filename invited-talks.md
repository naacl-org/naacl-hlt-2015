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

Abstract
: {{ talk[1].abstract }}

Biography
: {{ talk[1].biography }}

{% endfor %}
