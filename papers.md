---
title: Accepted papers
structure:
  - heading: "TACL Talks"
    key: tacltalks
  - heading: "TACL Posters"
    key: taclposters
  - heading: "Long Talks"
    key: longtalks
  - heading: "Long Posters"
    key: longposters
  - heading: "Short Talks"
    key: shorttalks
  - heading: "Short Posters"
    key: shortposters
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

{% for type in page.structure %}

## {{site.data.papers[type.key] | size}} {{type.heading}}

{% for paper in site.data.papers[type.key] %}

{{paper.authors}}. "*{{paper.title}}*"

{% endfor %}
{% endfor %}


