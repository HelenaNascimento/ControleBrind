from flask import Flask, Blueprint, render_template, session, redirect, url_for, flash, request
import pyodbc as bd
import pandas as pd

app = Flask(__name__)
app.secret_key = "supersecretkey"

def conexao():
    server = '192.186.11.15'
    database = 'BD_BRIND'
    cnxn = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.71;DATABASE=BD_BRIND;UID=sa;PWD=Infarma@2016.')
    return cnxn



televendas_bp = Blueprint('televendas', __name__)



if __name__ == '__main__':
    app.register_blueprint(televendas_bp)
    app.run(debug=True)
