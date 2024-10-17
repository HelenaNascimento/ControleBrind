from flask import Blueprint, render_template, session, redirect, url_for, flash

# Definindo o blueprint
televendas_bp = Blueprint('televendas', __name__)

@televendas_bp.route('/Pedido_Brinde')
def Pedido_Brinde():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('Televendas/televendas.html')
