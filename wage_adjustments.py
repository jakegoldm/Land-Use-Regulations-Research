import pandas as pd
import numpy as np

P = 2000

def wageadjustments(ya, la):
   wa = P * 0.75 * (ya / la)
   return wa

adjustments = [0.5, 0.75, 1, 1.25, 1.5]
for adjustment in adjustments:
   dfadjustedproductivity = pd.read_csv(
       "/Users/USER/Desktop/Research Spreadsheets/GDPProductivityAdjusted{}.csv".format(str(adjustment)), sep=",",
       index_col="Geography")
   dfadjustedemployment = pd.read_csv(
       "/Users/USER/Desktop/Research Spreadsheets/EmploymentAdjusted{}.csv".format(str(adjustment)), sep=",",
       index_col="Geography")
   dfwages = dfadjustedproductivity.copy(deep=True)
   rows, cols = dfwages.shape

   for row in range(rows):
       for col in range(cols):
           ya = dfadjustedproductivity.iat[row, col]
           la = dfadjustedemployment.iat[row, col]

           try:
               wa = wageadjustments(ya, la)
               dfwages.iat[row, col] = wa
           except Exception as ex:
               print(str(ex))
               dfwages.iat[row, col] = np.NaN

   outputfile = "/Users/USER/Desktop/Research Spreadsheets/GDPWagesAdjusted{}.csv".format(str(adjustment))
   print("generating outputfile " + outputfile)
   dfwages.to_csv(outputfile, sep=",")
