import pandas as pd
data = {
    "Student": ["Aman", "Priya", "Rohan", "Sneha", "Karan", "Simran", "Raj", "Neha"],
    "Math": [85, 78, 92, 88, 76, 65, 95, 82],
    "Science": [89, 74, 95, 80, 70, 60, 90, 85],
    "English": [78, 82, 88, 90, 75, 55, 85, 80]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
df = pd.read_csv("students.csv")
df["Average Marks"] = df.iloc[:, 1:].mean(axis=1)
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average Marks"].apply(assign_grade)
top_student = df.loc[df["Average Marks"].idxmax(), "Student"]
low_scorers = df[df["Average Marks"] < 60]["Student"].tolist()
print("\n Student Grades Analysis\n")
print(df)
print("\n🏆 Top Performer:", top_student)
print(f"\n Students scoring below 60: {', '.join(low_scorers) if low_scorers else 'None'}")
print("\nSummary Statistics:")
print(df.describe())
