
import pandas as pd

# Load the student dataset
df = pd.read_csv("student_analysis.csv")

print("Original dataset shape:", df.shape)

# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check duplicate rows
duplicate_count = df.duplicated().sum()
print("\nDuplicate rows:", duplicate_count)

# Remove duplicate rows
df = df.drop_duplicates()

# Check for invalid marks (marks should be between 0 and 100)
mark_columns = [
    "Math_Marks",
    "Science_Marks",
    "English_Marks"
]

for column in mark_columns:
    invalid_count = ((df[column] < 0) | (df[column] > 100)).sum()
    print(f"Invalid values in {column}: {invalid_count}")

# Display cleaned dataset information
print("\nCleaned dataset shape:", df.shape)
print("\nData cleaning completed successfully!")

# Student Performance Statistics

# Calculate each student's average marks
df["Average_Marks"] = df[
    ["Math_Marks", "Science_Marks", "English_Marks"]
].mean(axis=1)

# Calculate overall statistics
overall_average = df["Average_Marks"].mean()
highest_average = df["Average_Marks"].max()
lowest_average = df["Average_Marks"].min()

print("\n--- Student Performance Statistics ---")
print(f"Overall Average Marks: {overall_average:.2f}")
print(f"Highest Student Average: {highest_average:.2f}")
print(f"Lowest Student Average: {lowest_average:.2f}")

# Display each student's average
print("\nStudent-wise Average Marks:")
print(df[["Student_ID", "Average_Marks"]].to_string(index=False))

# Subject-Wise Performance Analysis

subjects = ["Math_Marks", "Science_Marks", "English_Marks"]

print("\n--- Subject-Wise Performance Analysis ---")

for subject in subjects:
    average = df[subject].mean()
    highest = df[subject].max()
    lowest = df[subject].min()

    print(f"\nSubject: {subject}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")

# Identify the subject with the highest class average
subject_averages = df[subjects].mean()
best_subject = subject_averages.idxmax()

print("\nSubject with Highest Class Average:", best_subject)

# Pass/Fail Analysis

PASS_MARK = 40

subjects = ["Math_Marks", "Science_Marks", "English_Marks"]

# A student passes only if they score at least 40 in every subject
df["Result"] = df[subjects].ge(PASS_MARK).all(axis=1).map(
    {True: "Pass", False: "Fail"}
)

total_students = len(df)
passed_students = (df["Result"] == "Pass").sum()
failed_students = (df["Result"] == "Fail").sum()

pass_percentage = (
    (passed_students / total_students) * 100
    if total_students > 0 else 0
)

print("\n--- Pass/Fail Analysis ---")
print("Total Students:", total_students)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print(f"Pass Percentage: {pass_percentage:.2f}%")

print("\nStudent Results:")
print(df[["Student_ID", "Result"]].to_string(index=False))

# Study Hours vs Performance Analysis

print("\n--- Study Hours vs Performance Analysis ---")

# Calculate average marks for each student
df["Average_Marks"] = df[
    ["Math_Marks", "Science_Marks", "English_Marks"]
].mean(axis=1)

# Calculate correlation between study hours and average marks
correlation = df["Study_Hours"].corr(df["Average_Marks"])

print(f"Correlation: {correlation:.2f}")

if correlation > 0:
    print("The dataset shows a positive relationship.")
elif correlation < 0:
    print("The dataset shows a negative relationship.")
else:
    print("No linear relationship detected in this dataset.")

# Compare average marks by study hours
study_analysis = df.groupby("Study_Hours")["Average_Marks"].mean()

print("\nAverage Marks by Study Hours:")
print(study_analysis.round(2))

import matplotlib.pyplot as plt

# Student Marks Distribution Chart

df["Average_Marks"] = df[
    ["Math_Marks", "Science_Marks", "English_Marks"]
].mean(axis=1)

plt.figure(figsize=(8, 5))

plt.hist(
    df["Average_Marks"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()

# Save chart to a file
plt.savefig("student_marks_distribution.png", dpi=300)

plt.show()

print("Chart saved as student_marks_distribution.png")


import matplotlib.pyplot as plt

# Visualize the distribution of student marks
plt.figure(figsize=(8, 5))

plt.hist(
    df["Average_Marks"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()

# Save the chart
plt.savefig("student_marks_distribution.png", dpi=300)

plt.show()

print("Student marks distribution chart saved successfully!")
