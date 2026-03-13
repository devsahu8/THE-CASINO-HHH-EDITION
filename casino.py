from app import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User

from app import create_app, db
app = create_app()

with app.app_context():
    db.create_all() # This creates your user/score tables in the cloud

if __name__ == "__main__":
    app.run()

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User}