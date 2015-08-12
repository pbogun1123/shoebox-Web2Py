# -*- coding: utf-8 -*-

def index():
    """ Displays most recent featured post on the index page """
    query = db(db.featuredPost).select(orderby=~db.featuredPost.postDate, limitby=(0,2))
    return dict(query = query)
    
def articles():
    """ Search all submitted articles """
    form = SQLFORM.factory(Field('keyword', requires=IS_NOT_EMPTY())).process()
    if form.accepted:
        query = db.articles.title.contains(form.vars.keyword)
        rows = db(query).select(orderby=~db.articles.articleDate)
    elif form.errors:
        response.flash = "Incomplete Search!"
        rows = ''
    else:
        rows = ''
    return dict(form=form, rows=rows)

def article_CLICK():
    """ Loads individual page for each article submitted to ShoeBox"""
    article_id = request.args(0, cast=int)
    article = db.articles(article_id) or redirect(URL('articles'))
    return dict(article = article)
    
def authors():
    """ Search all shoebox authors """
    form = SQLFORM.factory(Field('keyword', requires=IS_NOT_EMPTY())).process()
    if form.accepted:
        query = (((db.auth_user.first_name.contains(form.vars.keyword)) |
                (db.auth_user.last_name.contains(form.vars.keyword))) &
                (db.auth_user.is_author==True))
        rows = db(query).select(orderby=db.auth_user.last_name)
    elif form.errors:
        response.flash = "Incomplete Search!"
        rows = ''
    else:
        rows = ''
    return dict(form=form, rows=rows)

def authors_CLICK():
    """ Loads individual page for each ShoeBox author """
    author_id = request.args(0, cast=int)
    author = db.auth_user(author_id) or redirect(URL('articles'))
    query = db(db.articles.articleOwner==author_id).select()
    return dict(author = author, query = query, articles = articles)

def dashboard():
    """ Dashboard is a private view for Administrators that allows an easy
        interface for adding website content """
    return dict(grid=SQLFORM.smartgrid(db.featuredPost))
    
########## Extras ##########
    
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
