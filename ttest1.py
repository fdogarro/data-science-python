# import pandas for reading excel file
import pandas as pd
# import numpy for array data structure and methods
import numpy as np
# import ttest_ind to perform independent samples T-Test
from scipy.stats import ttest_ind

# Load sample data file
df = pd.read_excel('data/mpg.xlsx', engine='openpyxl')
# Convert miles column to 1-D np array
MilesPerGalon = np.array(df["Miles"])
print("Miles Per Galon: ", MilesPerGalon)
MilesPerGalon.shape
# Reshape arr to even 2-D arr
MilesArr = MilesPerGalon.reshape(2,79)
print("MilesArr: ", MilesArr)

# Boolean to indicate if equal variance is assumed
EqVariance = True
# Test equal variance is assumed or not by comparing larger std / smaller std
if MilesArr[0].std() > MilesArr[1].std():
    if(MilesArr[0].std() / MilesArr[1].std()) > 2:
        EqVariance = False
else:
    if(MilesArr[1].std() / MilesArr[0].std()) > 2:
        EqVariance = False

print("Equal Variance: ", EqVariance)

# Obtain the pvalue

SampleT = ttest_ind(MilesArr[0], MilesArr[1], equal_var=EqVariance)
print(SampleT, SampleT.pvalue)

# Determine if there is a difference between the samples

Significance = True
if SampleT.pvalue < 0.05:
    Significance = True
    print("Miles per gallon for US and Japanese cars are different")
else:
    Significance = False
    print("Miles per gallon for US and Japanese cars are the same")
