#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, FileSystemLoader

dest_path = os.path.join(os.path.dirname(__file__), './build')

env = Environment(loader=FileSystemLoader('%s/' % os.path.dirname(__file__)))

template = env.get_template('static_views/aboutus.html')
if not os.path.isdir(dest_path):
    os.makedirs(dest_path)
with open(os.path.join(dest_path, 'aboutus.html'), 'wb') as fp:
    fp.write(template.render().encode('utf-8'))
