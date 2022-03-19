import pandas as pd
import numpy as np

A = 25
def cobb_douglas(la, k):
   ya = A * (la ** 0.75) * (k ** 0.25)
   return ya

dfgdp = pd.read_csv("/Users/USER/Desktop/Research Spreadsheets/CountyGDPExtrapolated.csv", sep=",",
                   index_col="Geography")
g = dfgdp.lookup(["Fauquier County"], ["2001"])
adjustments = [0.5, 0.75, 1, 1.25, 1.5]

for adjustment in adjustments:
   dfadjustedemployment = pd.read_csv(
       "/Users/USER/Desktop/Research Spreadsheets/EmploymentAdjusted{}.csv".format(str(adjustment)), sep=",",
       index_col="Geography")
   dfproduct = dfadjustedemployment.copy(deep=True)
   rows, cols = dfproduct.shape

   for row in range(rows):
       for col in range(cols):
           la = dfadjustedemployment.iat[row, col]
           county = dfadjustedemployment.index.values[row]
           year = dfadjustedemployment.columns.values[col]

           try:
               k = dfgdp.lookup([county], [str(year)])
               k_value = k[0]
               ya = cobb_douglas(la, float(k_value))
               dfproduct.iat[row, col] = ya
           except Exception as ex:
               dfproduct.iat[row, col] = np.NaN

   dfproduct.to_csv("/Users/USER/Desktop/Research Spreadsheets/GDPProductivityAdjusted{}.csv".format(str(adjustment)),
                    sep=",")
