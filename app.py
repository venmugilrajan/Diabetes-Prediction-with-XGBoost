import gradio as gr
import pandas as pd
import pickle

# Load the trained model
with open("diabetes_xgboost.pkl", "rb") as f:
    model = pickle.load(f)

# Prediction function
def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
    input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]],
                              columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"])
    
    # Predict without scaling
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    if prediction == 1:
        return f"🔴 **Diabetes Detected!**\n\nRisk Probability: {probability:.2f}%"
    else:
        return f"🟢 **No Diabetes Detected.**\n\nRisk Probability: {probability:.2f}%"

# Gradio interface
interface = gr.Interface(
    fn=predict_diabetes,
    inputs=[gr.Number(label=c) for c in ["Pregnancies","Glucose","Blood Pressure","Skin Thickness","Insulin","BMI","Diabetes Pedigree Function","Age"]],
    outputs=gr.Markdown(label="Prediction Result"),
    title="🏥 Diabetes Prediction App",
    description="Enter patient health indicators to predict diabetes risk using a trained XGBoost model."
)

if __name__ == "__main__":
    interface.launch()
