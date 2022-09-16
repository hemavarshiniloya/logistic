
import streamlit as st
import pickel
pickel_in=open('Classifier.pkl','rb')
clf=pickel.load(pickel_in)
a=st.number_input('sepal lengthI(cm)')
b=st.number_input('sepal width(cm)')
c=st.number_input('sepal length(cm)')
d=st.number_input('sepal width(cm)')
r=' '
if st.button('PREDICT'):
    result=clf.predict([[a,b,c,d]]).squeeze()
    if result==0:
        st.success('SETOSA')
    elif result==0:
        st.success('VERSCOLOR')
    else:
        st.success('VIRGINCA')




