import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from collections import defaultdict

'''根据上一阶段热力图提供的数据，选取5个感兴趣且和第二日降水密切相关的特征
进行分地区分年份探索：Sunshine WindGustSpeed Humidity3pm Cloud3pm TempDiff'''
# 分地区：此处一个有趣的结果是 阳光和温差同时与第二天是否降水负相关，并且对于一个地区来讲，
# 这两个因素关于降水的相关性强弱同时增大，同时减小
df = pd.read_csv('processed_data_complete.csv', parse_dates=['Date'])
features_of_interest = ['Sunshine', 'WindGustSpeed', 'Humidity3pm', 'Cloud3pm', 'TempDiff']
# 分地区和特征 计算与RainTomorrow的相关系数
correlations = {}
for location in df['Location'].unique():
    correlations[location] = {}
    for feature in features_of_interest:
        location_data = df[df['Location'] == location]
        corr = location_data[feature].corr(location_data['RainTomorrow'])
        correlations[location][feature] = corr
corr_df = pd.DataFrame(correlations).T
plt.figure(figsize=(14, 7))
for feature in features_of_interest:
    plt.plot(corr_df.index, corr_df[feature], label=feature)
plt.legend()
plt.xlabel('Location')
plt.ylabel('Correlation with RainTomorrow')
plt.title('Correlation of Features with Rain Tomorrow by Location')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 绘制地图:每个地区的 TempDiff 相关系数，这里一个有意思的发现：越是北部相关性越弱
tempdiff_correlations = {location: correlations[location]['TempDiff'] for location in correlations}
australia_map = gpd.read_file('C:/Users/sun_e/Desktop/python/final/ausmap/gadm41_AUS_2.shp')
name_mapping_updated = {
    "Cobar": "New South Wales",
    "CoffsHarbour": "New South Wales",
    "Moree": "New South Wales",
    "NorfolkIsland": "Australian Capital Territory",
    "Sydney": "New South Wales",
    "SydneyAirport": "New South Wales",
    "WaggaWagga": "New South Wales",
    "Williamtown": "New South Wales",
    "Canberra": "Australian Capital Territory",
    "Sale": "Victoria",
    "MelbourneAirport": "Victoria",
    "Melbourne": "Victoria",
    "Mildura": "Victoria",
    "Portland": "Victoria",
    "Watsonia": "Victoria",
    "Brisbane": "Queensland",
    "Cairns": "Queensland",
    "Townsville": "Queensland",
    "MountGambier": "South Australia",
    "Nuriootpa": "South Australia",
    "Woomera": "South Australia",
    "PearceRAAF": "Western Australia",
    "PerthAirport": "Western Australia",
    "Perth": "Western Australia",
    "Hobart": "Tasmania",
    "AliceSprings": "Northern Territory",
    "Darwin": "Northern Territory"
}

tempdiff_correlations_updated = {name_mapping_updated.get(key, key): value for key, value in tempdiff_correlations.items()}
australia_map['TempDiff_Corr'] = australia_map['NAME_1'].map(tempdiff_correlations_updated)
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
australia_map.plot(column='TempDiff_Corr', ax=ax, legend=True, legend_kwds={'label': "Correlation with TempDiff"}, cmap='coolwarm')
plt.title('TempDiff Correlation with Rain Tomorrow by Location in Australia')
plt.show()


# 分年份:
# 选择一个位置
first_location = df['Location'].unique()[2]
df_first_location = df[df['Location'] == first_location]
df_first_location['Year'] = df_first_location['Date'].dt.year
# 计算每年的相关系数
yearly_correlations = {}
for year in df_first_location['Year'].unique():
    yearly_correlations[year] = {}
    year_data = df_first_location[df_first_location['Year'] == year]
    for feature in features_of_interest:
        corr = year_data[feature].corr(year_data['RainTomorrow'])
        yearly_correlations[year][feature] = corr
corr_yearly_df = pd.DataFrame(yearly_correlations).T
print(corr_yearly_df)
plt.figure(figsize=(14, 7))
for feature in corr_yearly_df.columns:
    plt.plot(corr_yearly_df.index, corr_yearly_df[feature], label=feature)
plt.legend()
plt.xlabel('Year')
plt.ylabel('Correlation with RainTomorrow')
plt.title('Yearly Correlation of Features with Rain Tomorrow at ' + first_location)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
