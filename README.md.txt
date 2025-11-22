# Student Academic Progress Tracker (SAPT) 🎓

**Course:** Introduction to Problem Solving and Programming 
**Student Name:** Vinayak
**Reg No:** 25BCY10210

## 📝 Project Overview
The Student Academic Progress Tracker (SAPT) is a Python-based command-line application designed to help first-year engineering students manage their academic records. It solves the problem of decentralized grade tracking by allowing students to store course details, calculate their SGPA automatically, and identify backlogs (failed courses) in real-time.

## ✨ Key Features
* **Course Management:** Add, View, and Delete course records.
* **Automated Calculation:** Instantly computes Semester Grade Point Average (SGPA) based on credits and marks.
* **Data Persistence:** All data is saved to a CSV file (`data/grades.csv`), ensuring records are not lost when the program closes.
* **Backlog Alert:** Automatically highlights courses where marks fall below the passing threshold.
* **Input Validation:** Robust error handling prevents the system from crashing if invalid data (like letters instead of numbers) is entered.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **File Handling:** CSV module (Standard Library)
* **Interface:** Command Line Interface (CLI)
* **Version Control:** Git & GitHub

## 🚀 Steps to Install & Run
1.  **Download the Project:**
    Clone this repository or download the ZIP file.
2.  **Open Terminal:**
    Navigate to the project folder via Command Prompt.
3.  **Run the Application:**
    Execute the following command:
    ```bash
    python src/main.py
    ```

## 🧪 How to Test
1.  Launch the application.
2.  Select **Option 2 (Add Course)** and enter:
    * Name: `Python Programming`
    * Credits: `4`
    * Marks: `85`
3.  Select **Option 4 (Generate Report)** to verify the GPA calculation.
4.  Select **Option 5 (Save & Exit)**.
5.  Relaunch the app and select **Option 1 (View)** to confirm the data was saved.

## 📸 Screenshots
*(Note to evaluator: Please see the Project Report PDF for detailed execution screenshots)*