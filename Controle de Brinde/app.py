from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
import pyodbc as bd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
