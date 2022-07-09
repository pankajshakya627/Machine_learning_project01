from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    return "Starting Machine Learning Project"


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='')