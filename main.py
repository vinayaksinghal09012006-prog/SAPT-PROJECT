import sys
from data_io import load_data, save_data
from course_manager import add_course, delete_course
from report_generator import show_all_courses, generate_summary

def main_menu():
    courses = load_data()
    
    while True:
        print("\n--- STUDENT ACADEMIC TRACKER (SAPT) ---")
        print("1. View All Courses")
        print("2. Add New Course")
        print("3. Delete Course")
        print("4. Generate GPA Report")
        print("5. Save & Exit")
        
        choice = input("Select Option (1-5): ")
        
        if choice == '1':
            show_all_courses(courses)
        elif choice == '2':
            add_course(courses)
        elif choice == '3':
            delete_course(courses)
        elif choice == '4':
            generate_summary(courses)
        elif choice == '5':
            save_data(courses)
            print("Exiting system. Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()