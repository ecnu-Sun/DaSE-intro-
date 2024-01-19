import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('processed_data_complete.csv', parse_dates=['Date'])
X = df.drop(['Date', 'RainTomorrow', 'Location', 'Temp9am', 'WindSpeed9am', 'TempDiff', 'PressureDiff', 'HumidityDiff'],
            axis=1)
y = df['RainTomorrow']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
# 神经网络
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(128, activation='sigmoid'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=20)
loss, accuracy = model.evaluate(X_test, y_test)
print(f"测试集上的损失: {loss}  准确率: {accuracy}")
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)
print(classification_report(y_test, y_pred, target_names=['Class 0', 'Class 1']))
with open('trained_models/neural_net_model.pkl', 'wb') as file:
    pickle.dump(model, file)
# xgboost
predictions = model.predict(X_test)
predicted_classes = (predictions > 0.5).astype(int)
predicted_probabilities = predictions
dtrain = xgb.DMatrix(X_train, label=y_train)
params = {
    'max_depth': 3,
    'eta': 0.1,
    'objective': 'binary:logistic',
    'eval_metric': 'logloss'
}
bst = xgb.train(params, dtrain, num_boost_round=100)
dtest = xgb.DMatrix(X_test)
preds = bst.predict(dtest)
predictions = [round(value) for value in preds]
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
bst.save_model('xgb_model.json')
