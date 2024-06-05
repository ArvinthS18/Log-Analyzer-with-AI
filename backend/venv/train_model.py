import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib

# Load your dataset
df = pd.read_csv(r'C:\Users\Aravindan\test1\backend\venv\error_logs.csv')

# Assuming your dataset has columns 'message' and 'error_type'
X = df['message']
y = df['error_type']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a pipeline: vectorizer => classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl')


# Evaluate the model (optional)
y_pred = model.predict(X_test)
print(metrics.classification_report(y_test, y_pred))

# # Example prediction on new message (optional)
# new_message = ".740169 #NORMAL #WARN : restartRawSocket returning!!"
# predicted_category = model.predict([new_message])
# print(f"Predicted error type for '{new_message}': {predicted_category[0]}")
