import pickle
from scipy.stats import mode
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('processed_data_complete.csv', parse_dates=['Date'])
# 特征和目标变量
X = df.drop(['Date', 'Location', 'RainTomorrow'], axis=1)
y = df['RainTomorrow']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.12, random_state=42)
# 逻辑回归模型
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)
y_pred_proba_lr = lr_model.predict_proba(X_test)[:, 1]
new_threshold = 0.47
y_pred_lr_new = (y_pred_proba_lr >= new_threshold).astype(int)
print("Logistic Regression Accuracy with New Threshold:", accuracy_score(y_test, y_pred_lr_new))
print(classification_report(y_test, y_pred_lr_new))
print("Logistic Regression Coefficients:", lr_model.coef_)
print("Logistic Regression Intercept:", lr_model.intercept_)
# 随机森林模型
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
y_pred_proba_rf = rf_model.predict_proba(X_test)[:, 1]  # 获取类别1的概率
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))
print("Random Forest Number of Trees:", len(rf_model.estimators_))
print("Random Forest Parameters:", rf_model.get_params())
# 支持向量机模型
svm_model = SVC(probability=True, random_state=42)
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
y_pred_proba_svm = svm_model.predict_proba(X_test)[:, 1]  # 获取类别1的概率
print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))
print("Random Forest Number of Trees:", len(rf_model.estimators_))
print("Random Forest Parameters:", rf_model.get_params())
# 打印概率输出
# print("Logistic Regression Predicted Probabilities:\n", y_pred_proba_lr)
# print("Random Forest Predicted Probabilities:\n", y_pred_proba_rf)
# print("SVM Predicted Probabilities:\n", y_pred_proba_svm)

'''
组合模型：
'''
y_pred_lr = (y_pred_proba_lr >= new_threshold).astype(int)
y_pred_rf = rf_model.predict(X_test)
y_pred_svm = svm_model.predict(X_test)
combined_predictions = np.array([y_pred_lr, y_pred_rf, y_pred_svm])
final_predictions, _ = mode(combined_predictions, axis=0)
final_predictions = final_predictions.flatten()
# 评估组合模型的性能
print("Combined Model Accuracy:", accuracy_score(y_test, final_predictions))
print(classification_report(y_test, final_predictions))


# 保存逻辑回归模型
with open('logistic_regression_model.pkl', 'wb') as file:
    pickle.dump(lr_model, file)
# 保存随机森林模型
with open('random_forest_model.pkl', 'wb') as file:
    pickle.dump(rf_model, file)
# 保存SVM模型
with open('svm_model.pkl', 'wb') as file:
    pickle.dump(svm_model, file)
