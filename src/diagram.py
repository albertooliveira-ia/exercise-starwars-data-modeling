from flask import Flask
from models import db
from sqlalchemy_schemadisplay import create_schema_graph

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

with app.app_context():
    graph = create_schema_graph(
        metadata=db.metadata,
        engine=db.engine, 
        show_datatypes=True,
        show_indexes=False,
        rankdir='LR',
        concentrate=False
    )
    graph.write_png('diagram.png')
    print("Diagrama generado correctamente.")