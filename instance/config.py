POSTGRES = {
    'user': 'myuser',
    'pw': 'mypassword',
    'db': 'my_db',
    'host': 'my_host',
    'port': '5432',
}

db_url = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(POSTGRES['user'], POSTGRES['pw'], POSTGRES['host'], POSTGRES['port'], POSTGRES['db'])


SECRET_KEY = 'Secret Key'
SQLALCHEMY_DATABASE_URI = db_url
