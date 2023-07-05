from flask import Flask, render_template, redirect, request, flash, session
import sqlite3 as db


App = Flask(__name__)
App.config['SECRET_KEY'] = 'leonanadm'

# Função para verificar se o usuário está logado
def verificar_login():
    if 'usuario' not in session:
        return redirect('/')
    
    else:
        return redirect('/usuarios')


@App.route('/')
def home():
    return render_template('index.html')


@App.route('/mesas')
def mesas():
    return render_template('mesas.html')


@App.route('/comandas1')
def comandas():
    return render_template('comandas.html')
@App.route('/comandas2')
def comandas2():
    return render_template('comandas2.html')
@App.route('/comandas3')
def comandas3():
    return render_template('comandas3.html')
@App.route('/comandas4')
def comandas4():
    return render_template('comandas4.html')
@App.route('/comandas5')
def comandas5():
    return render_template('comandas5.html')
@App.route('/comandas6')
def comandas6():
    return render_template('comandas6.html')
@App.route('/comandas7')
def comandas7():
    return render_template('comandas7.html')
@App.route('/comandas8')
def comandas8():
    return render_template('comandas8.html')
@App.route('/comandas9')
def comandas9():
    return render_template('comandas9.html')
@App.route('/comandas10')
def comandas10():
    return render_template('comandas10.html')
@App.route('/comandas11')
def comandas11():
    return render_template('comandas11.html')
@App.route('/comandas12')
def comandas12():
    return render_template('comandas12.html')






if __name__ == "__main__":
    App.run(debug=True)