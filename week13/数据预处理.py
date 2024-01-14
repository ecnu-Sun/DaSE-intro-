import pandas as pd

# 读取数据集
data = pd.read_csv('C:/Users/sun_e/Desktop/python/week13/turnover.csv')

# 检查缺失值
data.isnull().sum()

# 将分类数据转换为数字格式(onehot编码)
data = pd.get_dummies(data, columns=['sales', 'salary'])


# 删除离群值
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


# 对每个数值型特征应用删除离群值的函数
numerical_features = ['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours',
                      'time_spend_company']
for feature in numerical_features:
    data = remove_outliers(data, feature)
