import pandas as pd
import numpy as np
import math
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('weatherdata.csv', na_values="NA", parse_dates=['Date'])

# 首先把方向数据转化为单位向量，把YES转化为1，NO转化为0，方便计算使用
wind_dir_to_vector = {
    'N': (0, 1),
    'NNE': (math.cos(math.radians(22.5)), math.sin(math.radians(22.5))),
    'NE': (math.cos(math.radians(45)), math.sin(math.radians(45))),
    'ENE': (math.cos(math.radians(67.5)), math.sin(math.radians(67.5))),
    'E': (1, 0),
    'ESE': (math.cos(math.radians(112.5)), math.sin(math.radians(112.5))),
    'SE': (math.cos(math.radians(135)), math.sin(math.radians(135))),
    'SSE': (math.cos(math.radians(157.5)), math.sin(math.radians(157.5))),
    'S': (0, -1),
    'SSW': (math.cos(math.radians(202.5)), math.sin(math.radians(202.5))),
    'SW': (math.cos(math.radians(225)), math.sin(math.radians(225))),
    'WSW': (math.cos(math.radians(247.5)), math.sin(math.radians(247.5))),
    'W': (-1, 0),
    'WNW': (math.cos(math.radians(292.5)), math.sin(math.radians(292.5))),
    'NW': (math.cos(math.radians(315)), math.sin(math.radians(315))),
    'NNW': (math.cos(math.radians(337.5)), math.sin(math.radians(337.5))),
    'NA': (None, None)
}


def convert_wind_direction(df, columns):
    for col in columns:
        df[col] = df[col].map(wind_dir_to_vector)
    return df


# 数据标准化，避免大绝对值数据对后续分析造成主导性影响
num_cols = df.select_dtypes(include=[np.number]).columns
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

df = convert_wind_direction(df, ['WindGustDir', 'WindDir9am', 'WindDir3pm'])
df = df.replace({'Yes': 1, 'No': 0})


def find_similar_record(base_record, comparison_df, features):
    """
    在comparison_df中找到与base_record在特定特征上最相似的记录
    """
    valid_comparison_full = comparison_df.dropna()
    valid_comparison = valid_comparison_full[features]
    if valid_comparison.empty:
        return None
    # 处理base_record中的NaN值
    base_record_filled = base_record[features].fillna(valid_comparison[features].mean())
    try:
        distances = euclidean_distances([base_record_filled.values], valid_comparison)
    except Exception as e:
        print("计算距离出错：", e)
        print(base_record_filled)
        return None
    min_index = np.argmin(distances)
    return valid_comparison_full.iloc[min_index]


# 计算每列的缺失值数量和缺失率
missing_values = df.isnull().sum()
missing_rate = df.isnull().mean() * 100
pd.set_option('display.max_columns', None)
print(df.head(50))
# 定义用于比较的特征
features = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'RainTomorrow', 'RainToday',
            'Humidity9am']

# 用于检测填充速度
i = 0

# 对每列进行处理
for col in df.columns:
    if missing_rate[col] < 15:
        # 对于缺失率低于15%的列，使用热卡填充
        for index, row in df[df[col].isnull()].iterrows():
            # 确定搜索范围：相同地点的所有年份的同一月份
            search_df = df[(df['Location'] == row['Location']) &
                           (df['Date'].dt.month == row['Date'].month)]
            similar_record = find_similar_record(row, search_df, features)
            if similar_record is not None:
                df.at[index, col] = similar_record[col]
                i = i + 1
                print(i)

df.to_csv('processed_data_phase1.csv', index=False)
