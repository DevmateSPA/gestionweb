from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db
from models.usuario import Usuario

bp = Blueprint('login', __name__, template_folder='../templates/login')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre_usuario = request.form['usuario']
        clave = request.form['clave']

        #usuario = Usuario.query.filter_by(usuario=nombre_usuario, clave=clave).first()
        usuario = Usuario(id=1, usuario="admin", clave="1234")
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.usuario
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('principal.index'))
        else:
            flash('Usuario o clave incorrectos', 'danger')
            return redirect(url_for('login.index'))

    return render_template('login/index.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente', 'info')
    return redirect(url_for('login.index'))