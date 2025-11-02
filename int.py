from flask import Flask, render_template, request, jsonify, render_template_string
import tkinter as tk

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main page.html')

@app.route('/interest_info')
def int_info():
    return render_template('interest_info.html')

@app.route('/interest_questions')
def int_questions():
    return render_template('interest_questions.html')

@app.route('/taxes_questions')
def taxes_questions():
    return render_template('taxes_questions.html')

@app.route('/win')
def won():
    return render_template('win.html')

if __name__ == '__main__':
    app.run(debug=True)


