import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE

'''
经过预处理并且构造衍生变量的数据已经不再有任何缺失值，并且特征已经全部标准化了，含62247条数据
剩余字段：MinTemp	MaxTemp	Rainfall	Evaporation	Sunshine	WindGustSpeed	
WindSpeed9am	WindSpeed3pm	Humidity9am	Humidity3pm	Pressure9am	
Pressure3pm	Cloud9am	Cloud3pm	Temp9am	Temp3pm	RainToday	RainTomorrow
TempDiff PressureDiff HumidityDiff

'''
df = pd.read_csv('processed_data_complete.csv', parse_dates=['Date'])

# 
tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsne_results = tsne.fit_transform(df.drop(['Date', 'Location'], axis=1))
df['tsne-one'] = tsne_results[:, 0]
df['tsne-two'] = tsne_results[:, 1]
plt.figure(figsize=(8, 6))
plt.scatter(df['tsne-one'], df['tsne-two'], alpha=0.5)
plt.title('t-SNE plot')
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.show()

# 热力图显示，数据的字段之间存在普遍联系，此处特别关注一个点：
# 衍生特征：温度差，对降水有很强的负面作用，差不多可以抵消云层量对于降水的正面作用
# 如果不构造衍生特征，这是不容易察觉到的，并且在生活中也不容易察觉
df = df.drop(['Date', 'Location'], axis=1)
correlation_matrix = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
