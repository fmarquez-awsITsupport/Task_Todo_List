from flask import (
    Blueprint, render_template, request, url_for, redirect, flash, session, g
)

from werkzeug.security import generate_password_hash, check_password_hash

from . models import User
from todor import db

bp = Blueprint('auth', __name__, url_prefix='/auth')# url principal todo

@bp.route('/register', methods = ('GET', 'POST'))#Vistas de la url principal todo a traves de Blue Print que segmenta las rutas
def register():
    if request.method == 'POST':
        username = request.form['username'] # Acceder a los datos enviados por formulario [POST]
        password = request.form['password']

       

        user = User(username, generate_password_hash(password))

        error = None

        user_name = User.query.filter_by(username = username).first() 
        if user_name == None: # despues de validar que el username no esta duplicado
            db.session.add(user) # Hace una conexión a la base de datos SQLite
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya esta registrado'

        flash(error)


        
    return render_template('auth/register.html')

@bp.route('/login', methods = ('GET', 'POST'))#Vistas de la url principal todo a traves de Blue Print que segmenta las rutas
def login():
    if request.method == 'POST':
        username = request.form['username'] # Acceder a los datos enviados por formulario [POST]
        password = request.form['password']

       

        error = None

        #Validar los dstos 

        user = User.query.filter_by(username = username).first() 
        if user == None:
            error = 'Nombre de usuario es incorrecto'
        elif not check_password_hash(user.password, password): #Primer password se recupera de la tabla user db y el 2 de HTML
            error ='Contraseña incorrecta'

        #Iniciar sesion
        if error is None: 
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))
            
       

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
    