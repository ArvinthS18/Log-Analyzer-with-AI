import re
import joblib
from threading import Lock

# Initialize the lock
lock = Lock()
# Assuming p is a global list
p = []

# Load the trained model
model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
model = joblib.load(model_path)

def analyze_and_add_to_list(timestamp, message):
    combined_message = f"{timestamp}: {message}"
    
    # Assuming your model expects a list of messages for prediction
    messages_to_predict = [combined_message]
    
    # Predict error type for the message
    predicted_error_types = model.predict(messages_to_predict)
    response_text = predicted_error_types[0]
    print(response_text)

# Example usage
timestamp = "2024-06-07 10:00:00"
message = "2021-03-27 03:03:04.236121 #NORMAL #WARN : restartRawSocket returning!!"
analyze_and_add_to_list(timestamp, message)

