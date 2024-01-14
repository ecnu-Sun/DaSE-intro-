import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Region": ["Anting"] * 10 + ["Jiadingxincheng"] * 10 + ["Nanxiang"] * 10,
    "Month": [9] * 30,
    "Price": [327, 272, 152, 222, 83, 186, 285, 430, 438, 347,
              463, 120, 76, 306, 645, 409, 545, 327, 153, 637,
              437, 582, 586, 100, 507, 575, 1100, 427, 653, 252],
    "Rooms": [5, 5, 3, 3, 6, 3, 5, 4, 5, 4,
              4, 5, 4, 3, 5, 5, 5, 5, 7, 5,
              4, 4, 4, 3, 4, 4, 5, 4, 5, 3],
    "Area": [98, 91, 53, 63, 38, 73, 141, 119, 133, 98,
             90, 62, 42, 70, 130, 89, 111, 110, 59, 134,
             75, 88, 96, 36, 81, 89, 140, 86, 113, 59]
}
df = pd.DataFrame(data)
plt.figure(figsize=(18, 6))

# Matplotlib: Region
plt.subplot(1, 3, 1)
df.groupby('Region')['Price'].mean().plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Average Price by Region')
plt.ylabel('Average Price')

# Matplotlib: Price vs Area
plt.subplot(1, 3, 2)
plt.scatter(df['Area'], df['Price'], c=df['Rooms'], cmap='viridis')
plt.title('Price vs Area by Number of Rooms')
plt.xlabel('Area')
plt.ylabel('Price')
plt.colorbar(label='Number of Rooms')

# Matplotlib: Prices
plt.subplot(1, 3, 3)
plt.hist(df['Price'], bins=10, color='orange')
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

plt.figure(figsize=(18, 6))

# Seaborn:  Region
plt.subplot(1, 3, 1)
sns.barplot(x='Region', y='Price', data=df, ci=None)
plt.title('Average Price by Region')

# Seaborn: Price vs Area
plt.subplot(1, 3, 2)
sns.scatterplot(x='Area', y='Price', hue='Rooms', data=df, palette='coolwarm')
plt.title('Price vs Area by Number of Rooms')

# Seaborn:  Prices
plt.subplot(1, 3, 3)
sns.histplot(df['Price'], kde=True, color='purple')
plt.title('Distribution of Prices')

plt.tight_layout()
plt.show()