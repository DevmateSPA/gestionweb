from flask import Blueprint, render_template, session, redirect, url_for

bp = Blueprint('principal', __name__, template_folder='../templates/principal')

@bp.route('/')
def index():
    if 'usuario_id' not in session:
        return redirect(url_for('login.index'))
    return render_template('principal/index.html')
