from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.fotomecanica import Fotomecanica

bp = Blueprint('fotomecanica', __name__, template_folder='../templates/fotomecanica')

@bp.route('/')
def index():
    fotomecanicas = Fotomecanica.query.all()
    return render_template('fotomecanica/index.html', fotomecanicas=fotomecanicas)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nueva = Fotomecanica(
            codigo=request.form['codigo'],
            descripcion=request.form['descripcion']
        )
        db.session.add(nueva)
        db.session.commit()
        flash('✅ Fotomecánica agregada correctamente', 'success')
        return redirect(url_for('fotomecanica.index'))
    
    return render_template('fotomecanica/form.html', accion='Agregar')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    fotomecanica = Fotomecanica.query.get_or_404(id)
    if request.method == 'POST':
        fotomecanica.codigo = request.form['codigo']
        fotomecanica.descripcion = request.form['descripcion']
        db.session.commit()
        flash('✏️ Fotomecánica actualizada correctamente', 'success')
        return redirect(url_for('fotomecanica.index'))
    
    return render_template('fotomecanica/form.html', fotomecanica=fotomecanica, accion='Editar')

@bp.route('/delete/<int:id>')
def delete(id):
    fotomecanica = Fotomecanica.query.get_or_404(id)
    db.session.delete(fotomecanica)
    db.session.commit()
    flash('🗑️ Fotomecánica eliminada correctamente', 'danger')
    return redirect(url_for('fotomecanica.index'))
