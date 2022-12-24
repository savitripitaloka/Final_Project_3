import flask
from flask import request
import numpy as np
import pickle
import streamlit as st


# loading the saved model
model = pickle.load(open('D:/HACKTIV8/Final Project 3/Final_Project_3/model.pkl', 'rb'))


app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Age = int(request.form['Usia'])
    Ejection_Fraction = int(request.form['EF'])
    Serum_Creatinine = float(request.form['Serum_Kreatinin'])
    Serum_Sodium = float(request.form['Serum_Sodium'])
    predict_list = [[Age, Ejection_Fraction, Serum_Creatinine, Serum_Sodium]]
    prediction = model.predict(predict_list)
    output = {0: 'Not Died', 1: 'Died'}
    return flask.render_template('main.html', prediction_text='Prediction of Heart Failure Patient is {}'.format(output[prediction[0]]))