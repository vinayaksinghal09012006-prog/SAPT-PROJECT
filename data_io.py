import csv
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), '../data/grades.csv')

def load_data():
    """Loads courses from CSV file."""
    courses = []
    if not os.path.exists(FILE_PATH):
        return courses
    
    try:
        with open(FILE_PATH, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric strings back to numbers
                row['credits'] = float(row['credits'])
                row['marks'] = float(row['marks'])
                courses.append(row)
    except Exception as e:
        print(f"Error loading data: {e}")
    return courses

def save_data(courses):
    """Saves current list of courses to CSV."""
    try:
        with open(FILE_PATH, 'w', newline='') as file:
            fieldnames = ['name', 'credits', 'marks']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(courses)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")