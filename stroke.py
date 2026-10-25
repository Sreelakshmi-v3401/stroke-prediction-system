import streamlit as st
import pickle
from PIL import Image


#Load model files
model =pickle.load(open('stroke_model.save','rb'))
scalar=pickle.load(open('stroke_scalar.save','rb'))
encoded=pickle.load(open('encoded_gender.save','rb'))
encoded1=pickle.load(open('encoded_married.save','rb'))
encoded2=pickle.load(open('encoded_worktype.save','rb'))
encoded3=pickle.load(open('encoded_restype.save','rb'))
encoded4=pickle.load(open('encoded_smoking.save','rb'))

def main():
   st.title(':yellow[STROKE PREDICTION]')  

   img=Image.open('stroke image.png')
   st.image(img,width=600)

   #Inputs
   gender = st.selectbox(
   "enter your gender",
   ("Male", "Female"),)
   
   age =st.text_input('age','')

   hypertension = st.checkbox("Do you have a history of hypertension?")

   heart_disease=st.checkbox("Do you have heart disease")

   ever_married = st.selectbox("Have you ever been married?", ["No", "Yes"])

   work_type=st.selectbox("select worktype",['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
   
   Residence_type=st.selectbox("select Residence type", ['Urban', 'Rural'])

   avg_glucose_level =st.text_input('avg_glucose_level','')

   bmi =st.text_input('bmi','')

   smoking_status=st.selectbox("select smoking_status",['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

   #button
   pred=st.button('PREDICT')

   if pred:
      Gender=encoded.transform([gender])[0] 
      evrmarried=encoded1.transform([ever_married])[0]
      worktype=encoded2.transform([work_type])[0]  
      resitype=encoded3.transform([Residence_type])[0]
      smkinstts=encoded4.transform([smoking_status])[0]
     

      features = [
         [
             Gender,
             float(age),
             int(hypertension),
             int(heart_disease),
             evrmarried,
             worktype,
             resitype,
             float(avg_glucose_level),
             float(bmi),
             smkinstts,
         ]
     ]
                  
      scaled=scalar.transform(features)
      prediction=model.predict(scaled)



      if prediction[0] == 1:
          st.error('Warning: Stroke Detected')
      else:
          st.success('No Stroke Detected')
main()







 

  