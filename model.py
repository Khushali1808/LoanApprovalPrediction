import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset
data = pd.DataFrame({
    'income': [3000, 5000, 4000, 6000, 2000, 4500, 7000, 3500],
    'credit_score': [50, 80, 60, 90, 40, 70, 95, 55],
    'loan_amount': [10000, 20000, 15000, 25000, 5000, 18000, 30000, 12000],
    'loan_term': [12, 24, 18, 36, 12, 24, 36, 12],
    'approved': [0, 1, 0, 1, 0, 1, 1, 0]
})

X = data[['income','credit_score','loan_amount','loan_term']]
y = data['approved']

model = LogisticRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('loan_model.pkl', 'wb'))

print("Loan Approval Model trained and saved!")