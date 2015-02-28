---
title: Accepted papers
structure:
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

{% for type in page.structure %}

## {{site.data.papers[type.key] | size}} {{type.heading}}

{% for paper in site.data.papers[type.key] %}

{{paper.authors}}. "*{{paper.title}}*"

{% endfor %}
{% endfor %}


