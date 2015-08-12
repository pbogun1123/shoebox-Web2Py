
db.define_table(
    'articles',
    Field('title', requires = IS_NOT_EMPTY()),
    Field('articleContent', 'text', requires = IS_NOT_EMPTY()),
    Field('articleOwner', 'reference auth_user'),
    Field('articleDate', 'date', requires = IS_NOT_EMPTY()),
    format = '%(title)s: %(articleContent)s: %(owner_id)s')

db.define_table(
    'featuredPost',
    Field('postTitle', requires = IS_NOT_EMPTY(), label="Title"),
    Field('postContent', 'text', requires = IS_NOT_EMPTY(), label="Content"),
    Field('postAuthor', 'reference auth_user'),
    Field('postDate', 'date', requires = IS_NOT_EMPTY()),
    format = '%(postTitle)s: %(postContent)s: %(articleOwner)s')

############################################################

""" Populates tables with sample data """

if db(db.auth_user).isempty():
    import datetime
    from gluon.contrib.populate import populate
    pb_id = db.auth_user.insert(first_name = "Peter", last_name = 'Bogun',
                                email = 'peter.bogun@example.com',
                                password = CRYPT() ('test') [0])

    populate(db.auth_user, 50)
    db(db.auth_user.id <= 25).update(is_author = True)
