---
layout: default
title: CV
nav_key: cv
permalink: /cv/
---

# CV

<p class="cv-links">
  <a href="https://www.overleaf.com/read/kjsspxbkgdtk">Overleaf version</a>
  <span aria-hidden="true">|</span>
  <a href="https://scholar.google.nl/citations?user=vdV5FNsAAAAJ&hl=en">Google Scholar</a>
</p>

{% for section in site.data.cv %}
  <section class="cv-section">
    <h2>{{ section.title }}</h2>

    {% if section.type == "map" %}
      <div class="cv-card">
        <dl class="cv-map">
          {% for item in section.contents %}
            <dt>{{ item.name }}</dt>
            <dd>{{ item.value }}</dd>
          {% endfor %}
        </dl>
      </div>
    {% elsif section.type == "time_table" and section.render == "institution_list" %}
      <div class="cv-card">
        <ul class="cv-bullets cv-list">
          {% for item in section.contents %}
            <li>
              {% if item.institution contains "http" %}
                <a href="{{ item.institution }}">{{ item.institution | remove: "https://" | remove: "http://" }}</a>
              {% else %}
                {{ item.institution }}
              {% endif %}
              {% if item.year %} ({{ item.year }}){% endif %}
              {% if item.description %}
                {% if item.description_format == "paragraph" %}
                  <p class="cv-item-body">{{ item.description | join: " " }}</p>
                {% else %}
                  <ul class="cv-bullets">
                    {% for desc in item.description %}
                      <li>{{ desc }}</li>
                    {% endfor %}
                  </ul>
                {% endif %}
              {% endif %}
            </li>
          {% endfor %}
        </ul>
      </div>
    {% elsif section.type == "time_table" and section.render == "yearly_items" %}
      <div class="cv-card">
        <ul class="cv-bullets cv-list">
          {% for item in section.contents %}
            <li>
              {% if item.year %}<strong>{{ item.year }}:</strong>{% endif %}
              {% if item.items %}
                <ul class="cv-bullets cv-yearly-items">
                  {% for grant in item.items %}
                    <li>
                      {% if grant.url %}
                        {% if grant.text_before or grant.link_text or grant.text_after %}
                          {{ grant.text_before }}<a href="{{ grant.url }}">{{ grant.link_text | default: grant.text | default: grant.title }}</a>{{ grant.text_after }}
                        {% else %}
                          <a href="{{ grant.url }}">{{ grant.text | default: grant.title }}</a>
                        {% endif %}
                      {% elsif grant.text %}
                        {{ grant.text }}
                      {% else %}
                        {{ grant }}
                      {% endif %}
                    </li>
                  {% endfor %}
                </ul>
              {% elsif item.title %}
                {{ item.title }}
              {% endif %}
            </li>
          {% endfor %}
        </ul>
      </div>
    {% elsif section.type == "time_table" %}
      <div class="cv-card">
        <ul class="cv-timeline">
          {% for item in section.contents %}
            <li class="cv-timeline-item">
              <div class="cv-timeline-head">
                {% if item.title %}
                  <p class="cv-item-title">{{ item.title }}</p>
                {% elsif item.year %}
                  <p class="cv-item-title">{{ item.year }}</p>
                {% endif %}
                {% if item.title and item.year %}
                  <p class="cv-item-year">{{ item.year }}</p>
                {% endif %}
              </div>

              {% if item.institution %}
                <p class="cv-item-meta">
                  {% if item.institution contains "http" %}
                    <a href="{{ item.institution }}">{{ item.institution | remove: "https://" | remove: "http://" }}</a>
                  {% else %}
                    {{ item.institution }}
                  {% endif %}
                </p>
              {% endif %}

              {% if item.description %}
                {% if item.description_format == "paragraph" %}
                  <p class="cv-item-body">{{ item.description | join: " " }}</p>
                {% else %}
                  <ul class="cv-bullets">
                    {% for desc in item.description %}
                      <li>{{ desc }}</li>
                    {% endfor %}
                  </ul>
                {% endif %}
              {% endif %}

              {% if item.items %}
                <ul class="cv-bullets">
                  {% for bullet in item.items %}
                    <li>{{ bullet }}</li>
                  {% endfor %}
                </ul>
              {% endif %}
            </li>
          {% endfor %}
        </ul>
      </div>
    {% elsif section.type == "list" %}
      <div class="cv-card">
        <ul class="cv-bullets cv-list">
          {% for item in section.contents %}
            <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
    {% endif %}
  </section>
{% endfor %}
