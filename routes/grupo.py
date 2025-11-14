from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.grupo import Grupo

bp = Blueprint('grupo', __name__, template_folder='../templates/grupo')

@bp.route('/')
def index():
    grupos = Grupo.query.all()
    return render_template('grupo/index.html', grupos=grupos)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        codigo = request.form['codigo']
        descripcion = request.form['descripcion']

        nuevo_grupo = Grupo(codigo=codigo, descripcion=descripcion)
        db.session.add(nuevo_grupo)
        db.session.commit()

        flash('✅ Grupo creado correctamente', 'success')
        return redirect(url_for('grupo.index'))

    return render_template('grupo/form.html', accion='Crear')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    grupo = Grupo.query.get_or_404(id)

    if request.method == 'POST':
        grupo.codigo = request.form['codigo']
        grupo.descripcion = request.form['descripcion']
        db.session.commit()

        flash('✏️ Grupo actualizado correctamente', 'success')
        return redirect(url_for('grupo.index'))

    return render_template('grupo/form.html', grupo=grupo, accion='Editar')

@bp.route('/delete/<int:id>')
def delete(id):
    grupo = Grupo.query.get_or_404(id)
    db.session.delete(grupo)
    db.session.commit()

    flash('🗑️ Grupo eliminado correctamente', 'danger')
    return redirect(url_for('grupo.index'))
