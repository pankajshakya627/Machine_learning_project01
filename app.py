import sys
from flask import Flask, render_template, request, redirect, session
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys) 
        logging.info(housing.error_message)
        logging.info("Testing logging module")
        
    return "CI/CD pipeline is working"


if __name__ == "__main__":
	app.run(debug=True)
