pip uninstall scikit-learn joblib
pip install scikit-learn==1.2.2 joblib==1.2.0


import streamlit as st
import sklearn
import joblib

st.write("scikit-learn version:", sklearn.__version__)
st.write("joblib version:", joblib.__version__)
