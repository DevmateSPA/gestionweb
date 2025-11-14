from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.producto import Producto

bp = Blueprint('producto', __name__, template_folder='../templates/producto')

@bp.route('/')
def index():
    productos = Producto.query.all()
    return render_template('producto/index.html', productos=productos)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nuevo = Producto(
            codigo=request.form['codigo'],
            descripcion=request.form['descripcion'],
            grupo=request.form['grupo'],
            stmi=request.form['stmi'],
            papel=request.form['papel'],
            dime=request.form['dime']
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('✅ Producto creado correctamente', 'success')
        return redirect(url_for('producto.index'))

    return render_template('producto/form.html', accion='Crear')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.codigo = request.form['codigo']
        producto.descripcion = request.form['descripcion']
        producto.grupo = request.form['grupo']
        producto.stmi = request.form['stmi']
        producto.papel = request.form['papel']
        producto.dime = request.form['dime']

        db.session.commit()
        flash('✏️ Producto actualizado correctamente', 'success')
        return redirect(url_for('producto.index'))

    return render_template('producto/form.html', producto=producto, accion='Editar')

@bp.route('/delete/<int:id>')
def delete(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('🗑️ Producto eliminado correctamente', 'danger')
    return redirect(url_for('producto.index'))
