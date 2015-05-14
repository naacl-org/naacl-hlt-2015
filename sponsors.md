---
title: Sponsors
---

<style type="text/css">
.page-content {
    max-width: 100em !important;
}
</style>

{% for type in site.data.sponsors.types %}

# {{ type }}

{% for sponsor in site.data.sponsors[type] %}<a href="{{ sponsor.url }}">
<img class="sponsorlogo" src="img/sponsors/{{ sponsor.logo }}" title="{{ sponsor.name }}">
</a>{% endfor %}

{% endfor %}
