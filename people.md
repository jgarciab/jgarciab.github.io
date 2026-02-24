---
layout: default
title: Team
nav_key: people
permalink: /people/
---

# Team

{% assign current_people = site.data.people | where: "status", "current" %}
{% assign previous_people = site.data.people | where: "status", "previous" %}

{% include people_grid.html people=current_people %}

<h2>Former</h2>
{% include people_grid.html people=previous_people %}

<h2>Other Supervision</h2>
{% assign other_supervision = site.data.other_master_students | sort: "period" | reverse %}
<ul class="item-list supervision-list">
  {% for item in other_supervision %}
    <li>
      <p class="item-title"><span class="item-year">{{ item.period }}</span>{{ item.label }}</p>
      {% if item.thesis_title and item.thesis_link %}
        <p><strong>Thesis:</strong> <a href="{{ item.thesis_link }}">{{ item.thesis_title }}</a></p>
      {% elsif item.thesis_title %}
        <p><strong>Thesis:</strong> {{ item.thesis_title }}</p>
      {% endif %}
      <p>{{ item.note }}</p>
    </li>
  {% endfor %}
</ul>
