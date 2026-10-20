
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

