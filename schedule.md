---
title: NAACL-HLT 2015 Main Program Schedule
---

<style type="text/css">
.page-content {
    max-width: 100em !important;
}
</style>

# NAACL HLT 2015 Main Program Schedule
{:.no_toc}

* Table of contents
{:toc}

> This schedule is interactive, you can click on a session to view the talks in that session, and you can click on a talk to see its abstract.

{% assign ncols = 3 %}
{% assign colwidth = 90 | divided_by:ncols %}
{% assign demos = site.data.schedule.demos %}
{% assign papers = site.data.schedule.papers %}
{% assign manualpapers = site.data.manualschedule.papers %}
{% assign schedule = site.data.schedule.schedule %}
{% assign manualschedule = site.data.manualschedule.schedule %}

{% for today in schedule %}

## {{ today.date | date: "%A, %B %-d" }}

<table class="schedule">
{% for session in today.schedule %}
{% assign class = session.class %}
<tr class="{{ class }} {{ session.parent }}">
<td class="time"><p>{{ session.time }}</p></td>

{% assign sessioninfo = manualschedule[today.date][session.time] %}

{% for col in session['row'] %}
<td {% if session['row'].size == 1 %} colspan="{{ ncols }}" {% else %} width="{{ colwidth }}%" {% endif %}>

{% if class == "session" %}
{% assign sessionindex = forloop.index0 %}
{% assign room = sessioninfo[sessionindex].room %}
{% assign chair = sessioninfo[sessionindex].chair %}
{% else %}
{% assign room = null %}
{% assign chair = null %}
{% endif %}

{% for item in col %}
{% if manualpapers[item.ref] %}{% assign it = manualpapers[item.ref] %}
{% elsif papers[item.ref] %}{% assign it = papers[item.ref] %}
{% elsif demos[item.ref] %}{% assign it = demos[item.ref] %}
{% else %}{% assign it = item %}{% endif %}

{% if it.abstract %}<div class="talkinfo">{% endif %}
<p>
{% if it.prefix %}{% assign prefix = it.prefix %}
{% else %}{% assign prefix = item.ref %}{% endif %}
{% if prefix %}<span class="{{class}}prefix">{{ prefix }}</span>:{% endif %}
<span class="{{class}}title">{{ it["title"] }}</span>{% if it['authors'] %}, by
<span class="{{class}}authors">{{ it['authors'] }}</span>{% endif %}
{% if room %} &mdash; {{ room }}{% endif %}
</p>

{% if chair %}<p><em>Chair:</em> {{ chair }}</p>{% endif %}

{% if it.abstract %}
<blockquote class="talkabstract">{{ it.abstract }}</blockquote>
</div>
{% endif %}
{% endfor %}
</td>
{% endfor %}

</tr>
{% endfor %}
</table>

{% endfor %}
