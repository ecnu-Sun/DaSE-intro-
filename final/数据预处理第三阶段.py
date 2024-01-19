import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

'''由于剩下的带有缺失值的行不多了，并且主要缺失集中在evaporation，所以本阶段采用神经网络技术预测缺失的evaporation
使用与evaporation最相关的几个特征来预测：MinTemp MaxTemp Sunshine WindGustSpeed Humidity9am Pressure3pm RainToday'''
df = pd.read_csv('processed_data_phase2.csv', na_values="NA", parse_dates=['Date'])
# 训练随即森林模型并测试
features = ['MinTemp', 'MaxTemp', 'Sunshine', 'WindGustSpeed', 'Humidity9am', 'Pressure3pm', 'RainToday']
target = 'Evaporation'
df_clean = df.dropna()
X = df_clean[features]
y = df_clean[target]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.15, random_state=0)
model = RandomForestRegressor(n_estimators=12, random_state=2)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("均方误差 (MSE):", mse)
missing_values = df[df[target].isna()]
missing_values_clean = missing_values.dropna(subset=[col for col in missing_values.columns if col != target])
missing_values_scaled = scaler.transform(missing_values_clean[features])
predicted_evaporation = model.predict(missing_values_scaled)
exit(0)
# 使用训练好的模型，填充缺失的 Evaporation
df.loc[missing_values_clean.index, target] = predicted_evaporation
df = df.dropna()
df.to_csv('processed_data_phase3.csv', index=False)
