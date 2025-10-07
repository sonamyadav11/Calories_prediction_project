This project aims to predict the number of calories burned during physical activities based on personal and exercise parameters. The model is built using XGBoost, a powerful gradient boosting algorithm known for its accuracy and efficiency.
Dataset

The dataset contains the following features:

Feature	Description
User_ID	Unique identifier for each user
Gender	Gender of the user (Male/Female)
Age	Age of the user (in years)
Height	Height of the user (in cm)
Weight	Weight of the user (in kg)
Duration	Duration of the exercise (in minutes)
Heart_Rate	Average heart rate during the activity (in bpm)
Body_Temp	Body temperature during the activity (in °C)
Calories	Target variable: Calories burned

The model considers both personal parameters (like Age, Gender, Height, Weight) and exercise-specific parameters (Duration, Heart_Rate, Body_Temp) to predict calorie expenditure.

Model

Algorithm: XGBoost Regressor

Reason for Choice: XGBoost handles tabular data efficiently, manages missing values, and provides high prediction accuracy.

Evaluation Metrics: Mean Squared Error (MSE), R² Score.
