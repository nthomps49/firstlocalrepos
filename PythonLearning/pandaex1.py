import pandas as pd
other_path = (r"C:\Users\natha\Documents\GitHub\firstlocalrepos\PythonLearning\auto.csv")
df = pd.read_csv(other_path, header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
# use dropna to remove null rows with axis=0 and column price in subset
df.dropna(subset=['price'], axis=0)
#print(df)
# save dataframe as csv file 
#df.to_csv(r"C:\Users\natha\Documents\GitHub\firstlocalrepos\PythonLearning\automobile.csv")
# print type of each column
#print(df.dtypes)
#print(df.describe(include = "all"))
# describe details on only columns you want to see
#print(df[['length','compression-ratio']].describe())
#print(df.info)
#print first row all columns:
#print first row specific column:
print(df.loc[0,'price'])
