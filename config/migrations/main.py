import os

from config.db.pool import db

def create_tables():
    with db:
        db.create_tables([])

if os.environ.get('ENV') == 'development':
    create_tables()