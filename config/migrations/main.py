from config.db.pool import db

def create_tables():
    with db:
        db.create_tables([])
