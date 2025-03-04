from flask import jsonify, request, Flask, render_template
import pickle
import numpy as np
import os

model_path= os.path.join(os.getcwd(), 'diabetes_model.pkl')

model= pickle.load(open(model_path, "rb"))
app= Flask(__name__)


@app.route('/')
def home():
    
    return render_template('index.html')  
    
      
@app.route("/predict", methods=['POST'])
def predict():
    try: 
        data_from_html= [float(request.form.get(i)) for i in ['Age', 'Pregnancies','BMI','Glucose','BloodPressure',
                                                       'HbA1c','LDL','HDL','Triglycerides','WaistCircumference',
                                                       'HipCircumference','WHR','FamilyHistory',
                                                       'DietType','Hypertension','MedicationUse']]
        print(data_from_html)
        prediction= model.predict([np.array(data_from_html)])
        result= "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
    except Exception as e:
        print(f"issue in code is {e}")
    
    return render_template('index.html', prediction= result)
    

if __name__ == "__main__":
    app.run(debug=True)
        
        
