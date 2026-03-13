import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'king-of-kings-key'
    
    # THE FIX: Try to find the Postgres URL from Vercel first
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False