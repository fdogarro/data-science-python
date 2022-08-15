# Submitted by Felicia O'Garro. This assignment was worked on with Jamal O'Garro and took about 3 hours to complete.
import numpy as np
import pandas as pd

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
    # created list to filter out additional columns generated
    teachers_list = ["last_name", "first_name", "county", "district", "school", "primary_job",
    "fte", "salary","certificate","subcategory","teaching_route","highly_qualified",
    "experience_district","experience_nj","experience_total"]
    # read csv
    df = pd.read_csv('data/teachers_list.csv', usecols=teachers_list, escapechar='\\')

    df['fte'] = remove_special_chars(df['fte'])
    df['salary'] = remove_special_chars(df['salary'])
    df['experience_district'] = remove_special_chars(df['experience_district'], 0)
    df['experience_nj'] = remove_special_chars(df['experience_nj'], 0)
    df['experience_total'] = remove_special_chars(df['experience_total'], 0)
    df['experience_total'] = remove_special_chars(df['experience_total'], 0)

    #convert column data types
    df['fte'] = convert_to_float(df['fte'])
    df['salary'] = convert_to_float(df['salary'])
    df['experience_district'] = convert_to_int(df['experience_district'])
    df['experience_nj'] = convert_to_int(df['experience_nj'])
    df['experience_total'] = convert_to_int(df['experience_total'])

    print(df.head())

    print(len(df))

    # Show the last name of the ones who make more than 150,000 but has less than 5 years of total experience
    filtered = df[(df['salary'] > 150000) & (df['experience_total'] < 5)]['last_name']
    print("Salary > 150,000, Experience < 5 years:", filtered)

    # Get the last name of School Psychologist that works in Atlantic City
    filtered = df[(df['primary_job'] == 'School Psychologist') & (df['district'] == 'Atlantic City')]['last_name']
    print("Psychologist in Atlantic City:", filtered)

    # Get the last name and salary of the lowest earner who works in Atlantic City
    filtered = df[(df['district'] == 'Atlantic City')]
    result = filtered[(filtered['salary'] == filtered['salary'].min())][['last_name', 'salary']]
    print("Lowest earner in Atlantic City:", result)

    #Get the last name of employees working in Passaic City with more than ten years of total experience.
    filtered = df[(df['district'] == 'Passaic City') & (df['experience_total'] > 10)]['last_name']
    print("Working in Passaic City, experience > 10 years", filtered)


if __name__ == '__main__':
    main()
