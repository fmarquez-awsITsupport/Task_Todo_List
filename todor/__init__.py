from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def create_app(): #Para instanciar todo lo de abajo

    app = Flask(__name__)

    #configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY= 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    )
    
    db.init_app(app)

    #Registrar Blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')#Creacion de una ruta de vista con un decorador
    def index (): #Creamos una funcion
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()

    return app