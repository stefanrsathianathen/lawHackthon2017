
from flask import Flask
from flask import render_template, request 
# import sqlite3 as sql
import random as r

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/index.html',
                           title='Home')

@app.route('/search',methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        try:
            # product = request.form['product']
            # c = request.form['country']
            # # home = request.form['home'] 
            # #drop1 = request.form['drop']   
            # msg = product
            cat = request.form['product']
            expor = request.form['country']

        except:
            # msg = "failed"
            # c = "Df"
            # # h = "fses"
            # drop1 = 'D'
            cat = "failed"
            expor = "no where"
        finally:
            if cat == "Food" and expor == "China":
                return render_template("searched.html",product = cat,country=expor)
            else:
                return render_template("404.html")
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()