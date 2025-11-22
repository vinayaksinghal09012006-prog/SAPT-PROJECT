from validation_utils import get_valid_number, get_non_empty_string

def add_course(courses):
    print("\n--- Add New Course ---")
    name = get_non_empty_string("Enter Course Name: ")
    credits = get_valid_number("Enter Credits (1-30): ", 1, 30, is_float=True)
    marks = get_valid_number("Enter Marks (0-100): ", 0, 100, is_float=True)
    
    new_course = {
        'name': name,
        'credits': credits,
        'marks': marks
    }
    courses.append(new_course)
    print(f"Course '{name}' added successfully.")

def delete_course(courses):
    print("\n--- Delete Course ---")
    if not courses:
        print("No courses to delete.")
        return

    name_to_delete = get_non_empty_string("Enter name of course to delete: ")
    
    # List comprehension to filter out the course
    initial_count = len(courses)
    courses[:] = [c for c in courses if c['name'].lower() != name_to_delete.lower()]
    
    if len(courses) < initial_count:
        print("Course deleted.")
    else:
        print("Course not found.")