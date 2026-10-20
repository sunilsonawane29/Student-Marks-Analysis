
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
