import pandas as pd
df = pd.read_csv("california_housing_train.csv")

# print(df.describe())

# print(df.head(15))

# print(df.columns)

# print(df.iloc[[0,1,3],[0,1,2]])

# print(df.loc[[0,1,3],['latitude','housing_median_age']])

# print(df.head())

# df = df.drop(['median_income'],axis=1)

# print(df.head())

# print(df['housing_median_age'].value_counts())