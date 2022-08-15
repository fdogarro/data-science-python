# import pandas for reading excel file
import pandas as pd
# import numpy for array data structure and methods
import numpy as np
# import ttest_rel to perform paired samples T-Test
from scipy.stats import ttest_rel

# Load sample data file
df = pd.read_excel('data/scores.xlsx', engine='openpyxl')
# Convert SAT scores columns to numpy arrays
SAT1 = np.array(df["SAT_Score_Attempt_1"])
SAT2 = np.array(df["SAT_Score_Attempt_2"])

print("SAT1 Scores: ", SAT1)
print("SAT2 Scores: ", SAT2)

# Obtain and store T-Test results

TestResults = ttest_rel(SAT1, SAT2)

print("TResults and Pvalue: ",TestResults, TestResults.pvalue)

# Show if there is a significant difference
Significance = True
if TestResults.pvalue < 0.05:
    Significance = True
    print("Performance for SAT Scores are different")
else:
    Significance = False
    print("Performance for SAT Scores are the same")
