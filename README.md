---

````markdown
---
title: "Diabetes Prediction with XGBoost"
emoji: "🏥"
colorFrom: "blue"
colorTo: "green"
sdk: "gradio"
app_file: "app.py"
---

# 🏥 Diabetes Prediction App (XGBoost)

This interactive web application predicts the likelihood of a patient having diabetes based on health indicators such as glucose levels, BMI, age, and more. Built using the Pima Indians Diabetes Database, the model employs the XGBoost algorithm for accurate and efficient predictions.

## 📊 Features

- **User-Friendly Interface**: Input health metrics and receive instant predictions.
- **Model Transparency**: Built on the XGBoost algorithm, known for its performance and interpretability.
- **Real-Time Results**: Get immediate feedback on diabetes risk probability.

## 🧪 Model Overview

- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Dataset**: Pima Indians Diabetes Database
- **Metrics**:
  - Accuracy: 0.77
  - Precision: 0.76
  - Recall: 0.75
  - F1-Score: 0.75
  - AUC: 0.84

## ⚙️ How It Works

1. **Input**: Enter values for the following health indicators:
   - Pregnancies
   - Glucose
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - BMI
   - Diabetes Pedigree Function
   - Age

2. **Processing**: The model processes the inputs using the trained XGBoost classifier.

3. **Output**: Receive a prediction indicating whether the individual is at risk of diabetes, along with the probability percentage.

## 🛠️ Technologies Used

- **Gradio**: For creating the interactive web interface.
- **XGBoost**: For building the predictive model.
- **Pandas & NumPy**: For data manipulation and processing.

## 🚀 How to Run Locally

1. Clone this repository:

   ```bash
   git clone https://huggingface.co/spaces/venmugilrajan/Diabetes_Prediction_with_XGBoost
   cd Diabetes_Prediction_with_XGBoost
````

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:7860` to use the app.

## 🌐 Access the App Online

You can also try the app directly in your browser without any setup by visiting:

👉 [https://huggingface.co/spaces/venmugilrajan/Diabetes_Prediction_with_XGBoost](https://huggingface.co/spaces/venmugilrajan/Diabetes_Prediction_with_XGBoost)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

