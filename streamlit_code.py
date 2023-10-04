import pandas as pd
import numpy as np
import joblib
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
from custom import CustomTransformer_cat

model = joblib.load('package.pkl')
data = pd.read_csv('dataset.txt')

def model_prediction(name,year,miles):
    new = [name,year,miles]
    new = pd.DataFrame([new],columns = ['Name','Year','Miles'])
    prediction = model.predict(new)
    return prediction
   
def front_page():
    st.title("Car Prediction")
    
    display = """
    <div style = 'background-color:blue;'>
    <h2 style = 'color:white;text-align:left;'>Car Price Prediction</h2>
    </div>
    """    
    name = st.selectbox("Select the car brand", np.unique(data['Name']))
    year = st.selectbox("Select the year",('2018','2020','2012','2019','2017','2016','2015','2014','2010','2013','2011','2021','2022','2009','2023'))
    miles = st.number_input("Enter the Miles your car travelled",min_value = 1)
                           
    result = ""
    if st.button("Click here to Know your car Price"):
       result = model_prediction(name,year,miles)
       st.write("Your approximate Car Price :",result)

if __name__ == 'main':
        front_page()
                        
    
                        