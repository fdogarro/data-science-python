# Submitted by Felicia O'Garro. This assignment was worked on with Jamal O'Garro and took about 2 hours to complete.
import numpy as np
import pandas as pd

# remove trailing and leading space
def remove_whitespace(df):
    for col in df.columns:
        df[col] = df[col].map(lambda x: x and type(x) == str and x.strip() or x)
    return df

# convert vals to float
def convert_to_float(series):
    result = series.map(float)
    return result

# convert vals to int
def convert_to_int(series):
    result = series.map(int)
    return result

# remove special characters
def remove_special_chars(series, replace_val=np.NaN):
    result = series.replace('[^A‐Za‐z0‐9]', replace_val,regex=True)
    return result

def main():
    # read csv
    df = pd.read_csv('data/nj_teachers_salaries.csv')

    # drop rows with NaNs
    df_copy = df.dropna()

    #remove special characters from columns with mixed types for conversions

    df_copy['fte'] = remove_special_chars(df_copy['fte'])
    df_copy['salary'] = remove_special_chars(df_copy['salary'])
    df_copy['experience_district'] = remove_special_chars(df_copy['experience_district'], 0)
    df_copy['experience_nj'] = remove_special_chars(df_copy['experience_nj'], 0)
    df_copy['experience_total'] = remove_special_chars(df_copy['experience_total'], 0)
    df_copy['experience_total'] = remove_special_chars(df_copy['experience_total'], 0)

    #convert column data types
    df_copy['fte'] = convert_to_float(df_copy['fte'])
    df_copy['salary'] = convert_to_float(df_copy['salary'])
    df_copy['experience_district'] = convert_to_int(df_copy['experience_district'])
    df_copy['experience_nj'] = convert_to_int(df_copy['experience_nj'])
    df_copy['experience_total'] = convert_to_int(df_copy['experience_total'])

    # remove whitespace from dataframe
    df_copy = remove_whitespace(df_copy)

    # drop rows with NaNs again

    df_copy = df_copy.dropna()

    df_copy.to_csv('data/copy_new_nj_teachers_salaries.csv')



if __name__ == '__main__':
    main()
