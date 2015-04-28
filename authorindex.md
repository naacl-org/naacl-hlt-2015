---
title: NAACL-HLT 2015 Author Index
---
# NAACL HLT 2015 Author Index
{:.no_toc}

* Table of contents
{:toc}

> This schedule is interactive, you can click on an author to view that author's papers. (Unfortunately, the TACL papers that are to be presented at NAACL 2015 are not included in this author index).

{% assign authorindex = site.data.schedule.authorindex %}
{% assign papers = site.data.schedule.papers %}

{% for indexgroup in authorindex %}

## {{ indexgroup.letter }}

{% for authorinfo in indexgroup.authors %}

<div class="talkinfo">
<p>
<strong>{{ authorinfo.author }}</strong>,
{{ authorinfo.affiliation }}
[{{ authorinfo.refs | join:", " }}]
</p>

{% for ref in authorinfo.refs %}
<p class="sessiontalkabstract">
<span class="talkprefix">{{ ref }}</span>:
<span class="talktitle">{{ papers[ref].title }}</span>{% if papers[ref].authors %}, by
<span class="talkauthors">{{ papers[ref].authors }}</span>{% endif %}
</p>
{% endfor %}
</div>

{% endfor %}
{% endfor %}

