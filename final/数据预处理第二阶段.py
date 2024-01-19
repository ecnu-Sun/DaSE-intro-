import pandas as pd
import ast
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

'''
由于sunshine和evaporation列有太多缺失数据（40%）以上，所以使用主成分分析技术，评估每个原始变量对每个主成分的贡献
希望如果这两列其实是无关紧要的，就删去这些特征，这样一来不用删掉太多数据行

'''
df = pd.read_csv('processed_data_phase1.csv', na_values="NA", parse_dates=['Date'])
# 单独统计每个字段的缺失值数量
evaporation_missing = df['Evaporation'].isna().sum()
sunshine_missing = df['Sunshine'].isna().sum()

# 统计同时缺失 Evaporation 和 Sunshine 的行数
both_missing = df[df['Evaporation'].isna() & df['Sunshine'].isna()].shape[0]

print(f"Evaporation 缺失行数: {evaporation_missing}")
print(f"Sunshine 缺失行数: {sunshine_missing}")
print(f"同时缺失 Evaporation 和 Sunshine 的行数: {both_missing}")

def convert_to_tuple(s):
    try:
        # 使用literal_eval来解析字符串
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        # 如果解析失败，返回原始字符串
        return s


# 仅使用完全没有缺失值的行进行PCA
df_complete = df.dropna()
# 为了进行主成分分析，拆分向量
df_complete['WindGustDir'] = df_complete['WindGustDir'].apply(convert_to_tuple)
df_complete['WindDir9am'] = df_complete['WindDir9am'].apply(convert_to_tuple)
df_complete['WindDir3pm'] = df_complete['WindDir3pm'].apply(convert_to_tuple)
df_complete['WindGustDir_X'] = df_complete['WindGustDir'].apply(lambda x: x[0])
df_complete['WindGustDir_Y'] = df_complete['WindGustDir'].apply(lambda x: x[1])
df_complete['WindDir9am_X'] = df_complete['WindDir9am'].apply(lambda x: x[0])
df_complete['WindDir9am_Y'] = df_complete['WindDir9am'].apply(lambda x: x[1])
df_complete['WindDir3pm_X'] = df_complete['WindDir3pm'].apply(lambda x: x[0])
df_complete['WindDir3pm_Y'] = df_complete['WindDir3pm'].apply(lambda x: x[1])

# 'WindDirX' 和 'WindDirY' 是风向的正弦和余弦分量
numeric_cols = ['WindGustDir_X', 'WindGustDir_Y', 'WindDir9am_X', 'WindDir9am_Y', 'WindDir3pm_X', 'WindDir3pm_Y'] \
               + df.select_dtypes(include=[np.number]).columns.tolist()

# 从完整数据中选择这些列
df_numeric = df_complete[numeric_cols]

# 4. 执行 PCA
pca = PCA(n_components=len(numeric_cols))
pca.fit(df_numeric)

# 计算主成分和原始特征之间的相关性
components_corr = pd.DataFrame(pca.components_, columns=numeric_cols)

explained_var_ratio = pca.explained_variance_ratio_
cumulative_var_ratio = np.cumsum(pca.explained_variance_ratio_)
# 创建一个条形图来显示每个主成分的方差比例
plt.figure(figsize=(15, 8))
plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.5, align='center')
plt.step(range(1, len(np.cumsum(pca.explained_variance_ratio_)) + 1), np.cumsum(pca.explained_variance_ratio_), where='mid')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')

for i, component in enumerate(pca.components_):
    most_contributing_feature = numeric_cols[np.argmax(np.abs(component))]
    y_position = pca.explained_variance_ratio_[i] + 0.02  # 计算y坐标位置
    x_position = i + 1 - 0.1
    plt.annotate(f"PC{i+1}-{most_contributing_feature}",
                 xy=(i + 1, pca.explained_variance_ratio_[i]),
                 xytext=(x_position, y_position),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 horizontalalignment='right', verticalalignment='bottom',
                 rotation=45)  #

plt.title('Explained Variance of Principal Components')
plt.show()

# 计算相关性矩阵
corr_matrix = df_numeric.corr()

# 创建一个热力图
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')

# 显示热力图
plt.show()
exit(0)
# 删除 Sunshine 缺失的行
df = df.dropna(subset=['Sunshine'])
# 删除风向列
df = df.drop(columns=['WindGustDir', 'WindDir9am', 'WindDir3pm'])
df.to_csv('processed_data_phase2.csv', index=False)

