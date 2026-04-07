# Documentation for Trained Models

## Description of `trained_models/` Directory
The `trained_models/` directory contains the saved versions of the machine learning models trained for predicting various diseases. Each model is serialized in a format that allows for easy loading and inference within the application.

## Model Naming Convention
Models are named using the following convention:
```
<model_name>_<version>.<file_extension>
```
For example, `decision_tree_v1.pkl` indicates that this is the first version of a Decision Tree model saved in pickle format.

## How to Load and Use Saved Models
To load and use the saved models within your application, you can follow these steps:
```python
import joblib

# Load the model
model = joblib.load('trained_models/decision_tree_v1.pkl')

# Use the model to make predictions
predictions = model.predict(input_data)
```
Ensure that you have the necessary libraries installed for loading the specific model type.

## Model Performance Metrics
The performance metrics for each model can be found in the training logs or directly from the model evaluation phase. Key metrics may include:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC Score

## Versioning Information
Models are versioned to keep track of changes and improvements. Each time a model is trained and saved, its version is incremented. It is crucial to document the changes made in each version for future reference.

## Supported Model Types
This system supports various machine learning models, including but not limited to:
- Decision Trees
- Random Forests
- Support Vector Machines
- Neural Networks
- Logistic Regression