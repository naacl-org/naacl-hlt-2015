---
title: Accepted papers
structure:
  - heading: "TACL Posters"
    key: taclposters
  - heading: "TACL Talks"
    key: tacltalks
  - heading: "Long Posters"
    key: longposters
  - heading: "Long Talks"
    key: longtalks
  - heading: "Short Posters"
    key: shortposters
  - heading: "Short Talks"
    key: shorttalks
---

# List of accepted papers
{:.no_toc}

* Table of contents
{:toc}

At the suggestion of the TACL co-editors-in-chief, the decision
between talk and poster for TACL papers was made using random
selection, with the exception of one paper that specifically requested
a poster presentation.

The decision between talk and poster for the NAACL 2015 long and
short papers was made by consolidating the area chair recommendation
(if any) and the reviewers choice on the review form and the final
decision was made by the program co-chairs.

We have posted detailed [instructions for oral and poster
presentations](presentation-instructions.html). Please read this
important information to make sure you are adequately prepared for
your presentation at NAACL HLT 2015.

The one-minute-madness slides for the poster sessions are now available:
[PDF set 1](slides/one-minute-slides-A.pdf) and [PDF set 2](slides/one-minute-slides-B.pdf).

> This schedule is interactive, you can click on a paper title to view its abstract.

{% assign papers = site.data.schedule.papers %}
{% for type in page.structure %}
{% assign thepapers = site.data.schedule.talktypes[type.key] %}

## {{ thepapers | size }} {{ type.heading }}

{% for id in thepapers %}

<div class="talkinfo">
<p>
<span class="talkauthors">{{ papers[id].authors }}</span>.
"<span class="talktitle">{{ papers[id].title }}</span>"
</p>
<blockquote class="talkabstract">{{ papers[id].abstract }}</blockquote>
</div>

{% endfor %}
{% endfor %}
