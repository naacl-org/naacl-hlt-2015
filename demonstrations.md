---
title: Accepted demonstrations
---

# List of accepted system demonstrations

The demonstrations will be presented as posters on Tuesday, June 2nd, from 17:00 to 20:00.

> This schedule is interactive, you can click on a demonstration to view its abstract.

{% assign demos = site.data.schedule.demos %}

## {{ demos | size }} System Demonstrations

{% for demo in demos %}

<div class="talkinfo">
<p>
<span class="talkauthors">{{ demo[1].authors }}</span>.
"<span class="talktitle">{{ demo[1].title }}</span>"
</p>
<blockquote class="talkabstract">{{ demo[1].abstract }}</blockquote>
</div>

{% endfor %}
