# 📊 Student Report Analyzer using Pandas

A beginner-friendly **Pandas** project that analyzes student marks from a CSV file. It calculates average marks, identifies the topper and lowest scorer, performs subject-wise analysis, assigns grades, and generates a final report in CSV format.

---

## 🚀 Features

* 📂 Read student data from a CSV file
* 🧮 Calculate average marks for each student
* 🏆 Find the topper
* 📉 Find the lowest scorer
* 📊 Perform subject-wise analysis

  * Highest marks
  * Lowest marks
  * Average marks
* 🎓 Assign grades based on average marks
* 💾 Export the final report as a new CSV file

---

## 🛠️ Technologies Used

* Python 3
* Pandas

---

## 📁 Project Structure

```text
Student-Report-Analyzer/
│── students.csv          # Input dataset
│── main.py               # Main Python script
│── Student_Report.csv    # Generated report
└── README.md             # Project documentation
```

---

## 📄 Sample Dataset

```csv
Name,Math,Science,English
Ashish,95,90,88
Rahul,80,75,78
Priya,92,96,94
Riya,70,65,72
```


2. Navigate to the project directory:

```bash
cd student-report-analyzer
```

3. Install the required library:

```bash
pip install pandas
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📌 Output

The program displays:

* Complete student dataset
* Average marks of each student
* Topper details
* Lowest scorer details
* Subject-wise statistics
* Grades of all students

Finally, it generates:

```text
Student_Report.csv
```

---

## 🎓 Grade Criteria

| Average Marks | Grade |
| ------------: | :---: |
|  90 and above |   A   |
|       75 – 89 |   B   |
|       60 – 74 |   C   |
|      Below 60 |   D   |

---

## 📊 Concepts Covered

* Reading CSV files using Pandas
* DataFrames
* Column selection
* Row-wise calculations
* Finding maximum and minimum values
* Mean calculations
* Custom functions
* Applying functions with `apply()`
* Loops
* Conditional statements
* Exporting data to CSV

---

## 📈 Future Improvements

* Add data visualizations using Matplotlib or Seaborn
* Create an interactive dashboard with Streamlit
* Accept user-uploaded CSV files
* Generate PDF reports
* Add subject-wise grade analysis
* Display charts for student performance

---

## 📸 Example Output

```text
Student Data:
--------------------------------------------------
Name      Math  Science  English
Ashish      95       90       88
Rahul       80       75       78
Priya       92       96       94

Average Marks:
Ashish : 91.00
Rahul  : 77.67
Priya  : 94.00

Topper:
Priya - 94.00

Lowest Scorer:
Rahul - 77.67

Report Generated Successfully!
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub. It helps support the project and encourages future improvements.
