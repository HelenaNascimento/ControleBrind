from flask import Blueprint, render_template, session, redirect, url_for, flash

# Definindo o blueprint
brinde_bp = Blueprint('brinde', __name__)

@brinde_bp.route('/Dash_Brinde')
def Dash_Brinde():
    if 'user_id' not in session:
        flash('Por favor, faça o login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('Brinde/brinde.html')
