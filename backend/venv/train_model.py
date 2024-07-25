# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import make_pipeline
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# import joblib

# # Load your dataset
# df = pd.read_csv(r'C:\Users\Aravindan\test1\backend\venv\error_logs.csv')

# # Assuming your dataset has columns 'message' and 'error_type'
# X = df['message']
# y = df['error_type']

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Build a pipeline: vectorizer => classifier
# model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# # Train the model
# model.fit(X_train, y_train)

# # Save the trained model to a file
# joblib.dump(model, r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl')


# # Evaluate the model (optional)
# y_pred = model.predict(X_test)
# print(metrics.classification_report(y_test, y_pred))

# # Example prediction on new message (optional)
# new_message = ".740169 #NORMAL #WARN : restartRawSocket returning!!"
# predicted_category = model.predict([new_message])
# print(f"Predicted error type for '{new_message}': {predicted_category[0]}")


#Hypreparameter Tuning 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
import joblib
from imblearn.over_sampling import RandomOverSampler

# Load your dataset
df = pd.read_csv(r'C:\Users\Aravindan\test1\backend\venv\error_logs.csv')

# Assuming your dataset has columns 'message' and 'error_type'
X = df['message']
y = df['error_type']

# Balance the dataset using RandomOverSampler
ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X.values.reshape(-1, 1), y)
X_resampled = X_resampled.flatten()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Hyperparameter tuning for TfidfVectorizer and MultinomialNB
pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())
parameters = {
    'tfidfvectorizer__ngram_range': [(1, 1), (1, 2), (1, 3)],
    'multinomialnb__alpha': [0.5, 1.0, 1.5]
}

grid_search = GridSearchCV(pipeline, parameters, cv=5)
grid_search.fit(X_train, y_train)

# Save the best model
best_model = grid_search.best_estimator_
joblib.dump(best_model, r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl')

# Evaluate the best model
y_pred = best_model.predict(X_test)
print(metrics.classification_report(y_test, y_pred)) 

# Creating a dictionary for exact matches
exact_match_dict = pd.Series(y_train.values, index=X_train).to_dict()

# Improved predict_error_type function using the dictionary
def predict_error_type_with_dict(message, exact_match_dict, model):
    # Check for exact match in dictionary
    if message in exact_match_dict:
        return exact_match_dict[message]
    else:
        # If no exact match, use the model to predict
        return model.predict([message])[0]

# Testing the improved function
new_message = "#HIGH #ERROR : proxy is off"
predicted_category = predict_error_type_with_dict(new_message, exact_match_dict, best_model)
print(f"Predicted error type for '{new_message}': {predicted_category}")
