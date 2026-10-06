import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "Student": ["Arun", "Bala", "Kavin", "Rahul", "Vijay",
                "Ajay", "Suresh", "Manoj", "Dinesh", "Hari"],
    "Marks": [85, 72, 90, 65, 78, 88, 55, 92, 70, 80],
    "Attendance": [95, 85, 98, 75, 88, 92, 70, 96, 80, 90],
    "Study_Hours": [6, 4, 7, 3, 5, 6, 2, 8, 4, 5]
}

df = pd.DataFrame(data)

print(df)

plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Attendance"])
plt.title("Student Attendance")
plt.xlabel("Student")
plt.ylabel("Attendance (%)")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Study_Hours"])
plt.title("Study Hours")
plt.xlabel("Student")
plt.ylabel("Study Hours")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.show()