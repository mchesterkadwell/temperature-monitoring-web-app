from app import create_app, db
from app.models import Reading

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Reading=Reading)
