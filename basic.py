import streamlit as st

import pikle

st.title('Netwrok Ad purchased or Not ')
c=['Purchased'],['Not Purchased']

#age=st.number_input("Enter Age of customer  ",0.0)
#salary=st.number_input("Enter Estimated Salary",0.0)

age=st.slider("Enter Age of customer  ",10,100)
salary=st.slider("Enter Estimated Salary",1500,15000)

loaded_model=pikle.load(open('fsk.pkl','rb'))

prediction= loaded_model.predict([[age,salary]])

st.write('Predicted class is : ',c[prediction[0]])
