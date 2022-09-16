
import streamlit as st
import pickle
pickle_in=open('Classifier.pkl','rb')
clf=pickle.load(pickle_in)
a=st.number_input('sepal length')
b=st.number_input('sepal width')
c=st.number_input('petal length')
d=st.number_input('petal width')
result=' '
if st.button('PREDICT'):
    result=clf.predict([[a,b,c,d]]).squeeze()
    if result==0:
        st.success('SETOSA')
    elif result==0:
        st.success('VERSCOLOR')
    else:
        st.success('VIRGINCA')




