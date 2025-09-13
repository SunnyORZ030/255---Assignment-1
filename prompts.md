# Prompts I used with ChatGPT (Titanic)

## 1) Project Setup (CRISP-DM framing)
You are a senior data scientist. Help me complete an end-to-end ML project on Kaggle Titanic.
- Target: Survived (0/1)
- Task: Binary classification
- Constraints: Python + pandas + scikit-learn, Colab-friendly
Return: A step-by-step plan + executable code cells.

## 2) EDA & Data Quality
Generate code to inspect distributions, missing values, target balance, and potential leakage. Explain each output in simple terms.

## 3) Preprocessing & Features
Build a ColumnTransformer for numeric (median impute + scale) and categorical (most_frequent + OneHot). Suggest simple engineered features if beneficial (e.g., FamilySize).

## 4) Modeling
Create a baseline Logistic Regression and compare with RandomForestClassifier. Use a dev set for model selection.

## 5) Evaluation
Print accuracy, F1(macro), ROC-AUC. Show a confusion matrix and ROC curve. Provide 4–6 bullet takeaways.

## 6) Export Artifacts
Save figures to `artifacts/` and summaries/tables to `results/`.

## 7) README Help
Draft a concise summary of problem, method, best model, metrics, and lessons learned.
