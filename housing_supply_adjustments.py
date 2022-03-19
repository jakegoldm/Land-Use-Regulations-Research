import pandas as pd

df2000 = pd.read_csv("/Users/USER/Desktop/Research Spreadsheets/Housing2000-2010.csv", sep=",",
                    index_col="Geography")
print(df2000)
df2010 = pd.read_csv("/Users/USER/Desktop/Research Spreadsheets/Housing2010-2018.csv", sep=",",
                    index_col="Geography")
print(df2010)
df1980 = pd.read_csv("/Users/USER/Desktop/Research Spreadsheets/Census1990Virginia.csv", sep=",",
                    index_col="Geography")
print(df1980)

df = pd.merge(df2000, df2010, how="inner", on="Geography")
df = pd.merge(df, df1980, how="inner", on="Geography")
df = df.reindex(sorted(df.columns), axis=1)
print(df)

df.to_csv("/Users/USER/Desktop/Research Spreadsheets/Housing1980-2018.csv", sep=",")
df2 = df.interpolate(method="linear", axis=1)
df2.to_csv("/Users/USER/Desktop/Research Spreadsheets/HousingLinearInterpolation.csv", sep=",")

adjustments=[0.5,0.75,1,1.25,1.5]
for adjustment in adjustments:
   df3 = df2.copy(deep=True)
   rows, cols = df3.shape
   for row in range(rows):
       for col in range(cols):
           new_value = df3.iat[row, col] * adjustment
           df3.iat[row, col] = new_value
   df3.to_csv("/Users/USER/Desktop/Research Spreadsheets/HousingAdjusted{}.csv".format(str(adjustment)), sep=",")
