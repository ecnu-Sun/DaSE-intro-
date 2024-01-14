import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer

# 加载数据集
file_path = "D:\\data\\wine.csv"
wine_data = pd.read_csv(file_path)

# 删除'quality'为空的行
wine_data = wine_data.dropna(subset=['quality'])
# 使用KNNImputer进行缺失值填充
# 策略是找到具有相同品质的最近邻居，使用其值来填充缺失数据
imputer = KNNImputer(n_neighbors=1)
# 仅选择'quality'非NaN的行进行插补
wine_data_imputed = wine_data.dropna(subset=['quality'])
imputed_data = imputer.fit_transform(wine_data_imputed)
# 从插补数据创建DataFrame
wine_data_imputed = pd.DataFrame(imputed_data, columns=wine_data.columns)



# 可视化 1: 葡萄酒品质分布直方图
plt.figure(figsize=(8, 6))
sns.histplot(wine_data_imputed['quality'], kde=False)
plt.title('Wine Quality Distribution')  # 图表标题
plt.xlabel('Quality')  # x轴标签
plt.ylabel('Frequency')  # y轴标签
plt.grid(True)  # 显示网格
plt.savefig('C:/Users/sun_e/Desktop/python/week10/wine_quality_histogram.png')  # 保存图像
plt.close()

# 可视化 2: 品质对应的酒精含量箱型图
plt.figure(figsize=(8, 6))
sns.boxplot(x='quality', y='alcohol', data=wine_data_imputed)
plt.title('Alcohol Content by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Alcohol')
plt.grid(True)
plt.savefig('C:/Users/sun_e/Desktop/python/week10/alcohol_quality_boxplot.png')
plt.close()

# 可视化 3: 固定酸度与pH值的散点图
plt.figure(figsize=(8, 6))
sns.scatterplot(x='fixed acidity', y='pH', hue='quality', data=wine_data_imputed, palette='viridis')
plt.title('pH vs Fixed Acidity')
plt.xlabel('Fixed Acidity')
plt.ylabel('pH')
plt.legend(title='Quality')
plt.grid(True)
plt.savefig('C:/Users/sun_e/Desktop/python/week10/pH_acidity_scatter.png')
plt.close()

# 可视化 4: 葡萄酒属性相关性热图
plt.figure(figsize=(8, 6))
sns.heatmap(wine_data_imputed.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Wine Attributes')
plt.savefig('C:/Users/sun_e/Desktop/python/week10/correlation_heatmap.png')
plt.close()

# 可视化 5: 品质对应的挥发性酸度小提琴图
plt.figure(figsize=(8, 6))
sns.violinplot(x='quality', y='volatile acidity', data=wine_data_imputed)
plt.title('Volatile Acidity by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Volatile Acidity')
plt.grid(True)
plt.savefig('C:/Users/sun_e/Desktop/python/week10/volatile_acidity_violin.png')
plt.close()


