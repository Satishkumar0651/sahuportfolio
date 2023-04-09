import pickle
import pandas as pd

def predict_ads(input_data):
    # Load the saved model
    with open('./models/model_logistic_regression.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # Create a dictionary to map categorical variables to numerical variables
    cat_map = {'Male': 1, 'Female': 0}
    month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    weekday_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    
    # print(input_data)
    # Convert categorical variables to numerical variables
    gender = cat_map[input_data["male"]]
    month = month_map[input_data["month"]]
    day = input_data["day"]
    weekday = weekday_map[input_data["weekday"]]
    hour = input_data["hour"]
    
    # Create a new DataFrame for prediction
    pred_df = pd.DataFrame({'Daily Time Spent on Site': input_data["daily_time_spent"], 'Age': input_data["age"], 'Area Income': input_data["area_income"],
                            'Daily Internet Usage': input_data["daily_internet_usage"], 'Male': gender, 'Month': month, 'Day': day,
                            'Weekday': weekday, 'Hour': hour}, index=[0])
    
    # Make the prediction and return the result
    prediction = model.predict(pred_df)
    # print("prediction done")
    return prediction[0]