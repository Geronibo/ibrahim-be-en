#!/usr/bin/env python
# coding: utf-8

import joblib

def predict(df):
    svm = joblib.load('svm_model.sav')
    return svm.predict(df)

    
   

