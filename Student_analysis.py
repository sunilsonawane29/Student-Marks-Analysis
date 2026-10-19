
import pandas as pd

data = {
    "Student": ["Amit", "Priya", "Rahul", "Sneha", "Rohit"],
    "Python": [78, 85, 45, 92, 32],
    "SQL": [80, 90, 50, 88, 35],
    "Excel": [75, 95, 55, 91, 40]
}

df = pd.DataFrame(data)

df["Average"] = df[["Python", "SQL", "Excel"]].mean(axis=1)
df["Result"] = df["Average"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print("STUDENT MARKS ANALYSIS")
print(df.to_string(index=False))

print("\nClass Average:", round(df["Average"].mean(), 2))
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

df.to_csv("student_analysis.csv", index=False)
print("\nResults saved to student_analysis.csv")
