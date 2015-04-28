---
title: Accepted demonstrations
---

# List of accepted system demonstrations

> This schedule is interactive, you can click on a demonstration to view its abstract.

{% for demo in site.data.schedule.demos %}

<div class="talkinfo">
<p>
<span class="talkauthors">{{ demo[1].authors }}</span>.
"<span class="talktitle">{{ demo[1].title }}</span>"
</p>
<blockquote class="sessiontalkabstract">{{ demo[1].abstract }}</blockquote>
</div>

{% endfor %}

