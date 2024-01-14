import pandas as pd

# 原始数据集
data = {
    "square_feet": [2000, 1600, 2200, 1800, 2400],
    "bedrooms": [3, 2, 4, 3, 4],
    "bathrooms": [2, 1, 3, 2, 3],
    "garage_area": [400, 250, 500, 350, 450],
    "basement_area": [600, 500, 800, 550, 700],
    "year_built": [1995, 1980, 2005, 1990, 2010],
    "house_type": ["Single Family", "Apartment", "Single Family", "Townhouse", "Single Family"],
    "neighborhood_quality": [8, 6, 9, 7, 8],
    "sale_price": [250000, 150000, 350000, 200000, 400000]
}

df = pd.DataFrame(data)
# 添加衍生特征如下：
# 总面积 : 房屋面积 车库面积 地下室面积之和
# 年龄 : 房屋的年龄
# 卧室和浴室比 : 卧室数量与浴室数量的比率 可以反应卧室配备的浴室的充裕情况
# 面积和房间数的比 : 可以反映单个房间的相对大小
# 价格每平方英尺 : 反映了单位价格高低
current_year = 2024
df['total_area'] = df['square_feet'] + df['garage_area'] + df['basement_area']
df['age'] = current_year - df['year_built']
df['bed_bath_ratio'] = df['bedrooms'] / df['bathrooms']
df['area_per_room'] = df['total_area'] / df['bedrooms']
df['price_per_sqft'] = df['sale_price'] / df['square_feet']
print(df)

