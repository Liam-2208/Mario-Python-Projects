import pandas as pd

# Creating a sample DataFrame with student information
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob', 'Charlie'],
        'Subject': ['Math', 'Math', 'Math', 'Math', 'English', 'English', 'English'],
        'Score': [80, 90, 75, 85, 85, 88, 92],
        'Attendance': [90, 95, 80, 92, 88, 93, 78]}


df = pd.DataFrame(data)

students = ['Alice', 'Bob', 'Charlie', 'David']
student_avg_grades = df.groupby('Name')['Score'].mean().sort_values(ascending=True)
print(round(student_avg_grades.iloc[-1], 2))




# Displaying the DataFrame
print("Original DataFrame:")
print(df)
print("\n")