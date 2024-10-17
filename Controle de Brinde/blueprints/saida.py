from flask import Blueprint, render_template, session, redirect, url_for, flash

# Definindo o blueprint
saida_bp = Blueprint('saida', __name__)

@saida_bp.route('/Sai_CB')
def Sai_CB():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('Saida/saida.html')
