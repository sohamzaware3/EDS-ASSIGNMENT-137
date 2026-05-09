import pandas as pd

print("PANDAS OPERATIONS")

series = pd.Series([10, 20, 30, 40, 50])

print("\nSeries:")
print(series)

data = {
    "Name": ["Amit", "Sara", "John", "Riya"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 88, 92]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nData Types:")
print(df.dtypes)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nIndex:")
print(df.index)

print("\nSelect Name Column:")
print(df["Name"])

print("\nFirst Row:")
print(df.iloc[0])

print("\nRows 1 to 2:")
print(df.iloc[1:3])

df["Grade"] = ["A", "A+", "A", "A+"]

print("\nAfter Adding Grade Column:")
print(df)

df.loc[0, "Marks"] = 95

print("\nAfter Updating Marks:")
print(df)

df = df.drop("Grade", axis=1)

print("\nAfter Deleting Grade Column:")
print(df)

print("\nMean Marks:")
print(df["Marks"].mean())

print("\nMaximum Marks:")
print(df["Marks"].max())

print("\nMinimum Marks:")
print(df["Marks"].min())

print("\nSum of Marks:")
print(df["Marks"].sum())

print("\nSorted by Marks:")
print(df.sort_values(by="Marks"))

print("\nStudents with Marks > 88:")
print(df[df["Marks"] > 88])

df.loc[2, "Marks"] = None

print("\nData with Missing Value:")
print(df)

print("\nFill Missing Values:")
print(df.fillna(0))

df.to_csv("students.csv", index=False)

print("\nCSV File Saved")

new_df = pd.read_csv("students.csv")

print("\nReading CSV File:")
print(new_df)

group_data = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 60000, 45000]
})

print("\nGroup By Department:")
print(group_data.groupby("Department").mean())

print("\nDescriptive Statistics:")
print(df.describe())