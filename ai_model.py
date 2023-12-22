```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Database connection setup
engine = create_engine('postgresql://username:password@localhost:5432/materials_db')

def load_data():
    """
    Function to load the preprocessed data from the database.
    """
    df = pd.read_sql('preprocessed_data', engine)
    return df

def split_data(df):
    """
    Function to split the data into training and testing sets.
    """
    X = df.drop('composition', axis=1)
    y = df['composition']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Function to train the AI model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Function to evaluate the model performance.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy}')

def save_model(model):
    """
    Function to save the trained model for future use.
    """
    with open('ai_model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model)
```
