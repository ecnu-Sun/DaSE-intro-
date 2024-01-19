import pandas as pd
'''
数据预处理后，简单地构造几个衍生特征：当日温差（TempDiff）当日气压差（PressureDiff）
当日湿度差（HumidityDiff）希望这些衍生特征在之后构建模型时可以产生作用
'''
df = pd.read_csv('processed_data_phase3.csv', parse_dates=['Date'])
df['TempDiff'] = df['MaxTemp'] - df['MinTemp']
df['PressureDiff'] = df['Pressure3pm'] - df['Pressure9am']
df['HumidityDiff'] = df['Humidity3pm'] - df['Humidity9am']
df.to_csv('processed_data_complete.csv', index=False)