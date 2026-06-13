---
layout: default
title: Apps
nav_key: apps
permalink: /apps/
---

# Apps

<p>Interactive Marimo apps for teaching core ideas in prediction, network science, and computational social science.</p>

<h2>Machine Learning</h2>
<div class="tiles-grid apps-grid apps-topic-grid">
  {% assign machine_learning_apps = site.data.apps | where: "topic", "Machine Learning" %}
  {% for item in machine_learning_apps %}
    {% include app_tile.html item=item %}
  {% endfor %}
</div>

<h2>Networks</h2>
<div class="tiles-grid apps-grid apps-topic-grid">
  {% assign network_apps = site.data.apps | where: "topic", "Networks" %}
  {% for item in network_apps %}
    {% include app_tile.html item=item %}
  {% endfor %}
</div>
