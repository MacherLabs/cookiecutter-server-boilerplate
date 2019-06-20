#!/bin/sh

{% if cookiecutter.framework == "flask" %}
pip install -e .
{% elif cookiecutter.framework == "express" %}
npm install
{% else %}
#  Install depedencies etc over here. 
{% endif %}