import pandas as pd


df = pd.read_csv("/Users/aashishmewada/Desktop/p2/Pandas/pandas1/students.csv")

print("\nStudent Data:")
print(df)


df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\nAverage Marks:")
print(df[["Name", "Average"]])

# Topper
topper = df.loc[df["Average"].idxmax()]

print("\nTopper:")
print(topper["Name"], "-", round(topper["Average"], 2))


lowest = df.loc[df["Average"].idxmin()]

print("\nLowest Scorer:")
print(lowest["Name"], "-", round(lowest["Average"], 2))


print("\nSubject Analysis")

subjects = ["Math", "Science", "English"]

for subject in subjects:
    print(f"\n{subject}")
    print("Highest:", df[subject].max())
    print("Lowest :", df[subject].min())
    print("Average:", round(df[subject].mean(), 2))


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)

print("\nGrades:")
print(df[["Name", "Average", "Grade"]])


df.to_csv("Student_Report.csv", index=False)

print("\nReport Generated Successfully!")