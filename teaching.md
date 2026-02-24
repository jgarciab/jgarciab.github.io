---
layout: default
title: Teaching
nav_key: teaching
permalink: /teaching/
---

# Teaching

<p>Click on the tiles below to access course websites and materials.</p>
<div class="tiles-grid">
  {% for item in site.data.teaching_main %}
    {% include teaching_tile.html item=item %}
  {% endfor %}
</div>

<h2>Other Courses and Workshops</h2>
<ul class="item-list">
  {% for item in site.data.teaching_other %}
    <li>
      <p class="item-title"><a href="{{ item.url }}">{{ item.title }}</a>{% if item.institution %} <span class="muted institution-note">({{ item.institution }})</span>{% endif %}</p>
      <p class="item-meta">{{ item.note }}</p>
    </li>
  {% endfor %}
</ul>
