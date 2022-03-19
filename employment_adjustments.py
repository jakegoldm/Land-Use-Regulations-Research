import pandas as pd
import numpy as np

adjustment = 1
dfemployment = pd.read_csv("/Users/USER/Desktop/Research Spreadsheets/EmploymentUnadjusted1990-2018.csv", sep=",")
dfunadjustedhousing = pd.read_csv("/Users/USER/Desktop/Research Spreadsheets/HousingLinearInterpolation.csv", sep=",",
                                 index_col="Geography")

adjustments = [0.5, 0.75, 1, 1.25, 1.5]
for adjustment in adjustments:
   dfadjustedhousing = pd.read_csv(
       "/Users/USER/Desktop/Research Spreadsheets/HousingAdjusted{}.csv".format(str(adjustment)), sep=",",
       index_col="Geography")
   df3 = dfadjustedhousing.copy(deep=True)
   rows, cols = df3.shape

   for row in range(rows):
       for col in range(cols):
           unadjustedhousing_value = dfunadjustedhousing.iat[row, col]
           adjustedhousing_value = dfadjustedhousing.iat[row, col]
           county = dfadjustedhousing.index.values[row]
           year = dfadjustedhousing.columns.values[col]

           try:
               q = "Year == {} and Geography == '{}'".format(year, county)
               employment = dfemployment.query(q)
               if not employment.empty:
                   employment_value = employment.iat[0,1]
                   la = (adjustedhousing_value/unadjustedhousing_value) * employment_value
                   df3.iat[row,col] = la
               else:
                   df3.iat[row,col] = np.NaN
           except Exception as ex:
               print (str(ex))

   df3.to_csv("/Users/USER/Desktop/Research Spreadsheets/EmploymentAdjusted{}.csv".format(str(adjustment)), sep=",")
