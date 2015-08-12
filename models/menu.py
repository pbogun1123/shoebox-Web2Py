# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('ShoeBox'),XML('&trade;&nbsp;'),
                  _class="brand",_href="http://127.0.0.1:8000/shoebox")

## response.title = 'This is the response.title in models/menu.py'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    ('Home', False, URL('default', 'index')),
    ('Articles', False, URL('default', 'articles')),
    ('Authors', False, URL('default', 'authors'))]

if auth.user and auth.user.is_administrator:
    response.menu.append(('Dashboard', False, 'dashboard'))

if False:
    auth.wikimenu()
