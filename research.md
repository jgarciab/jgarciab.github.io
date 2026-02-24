---
layout: default
title: Research
nav_key: research
permalink: /research/
---

# Research

<p>
  Explore the tiles below for a concise overview of my main research areas and ongoing lines of work.
</p>

{% assign current_projects = site.data.research | where: "status", "current" %}
{% assign previous_projects = site.data.research | where: "status", "previous" %}

<div class="tiles-grid">
  {% for item in current_projects %}
    {% include research_tile.html item=item %}
  {% endfor %}
</div>

<h2>Previous Projects</h2>
<div class="tiles-grid">
  {% for item in previous_projects %}
    {% include research_tile.html item=item %}
  {% endfor %}
</div>
