from gpa_calculator import calculate_sgpa, check_backlogs, get_grade_point

def show_all_courses(courses):
    print("\n" + "="*50)
    print(f"{'Course Name':<20} | {'Credits':<8} | {'Marks':<6} | {'Grade Pt':<8}")
    print("-" * 50)
    
    if not courses:
        print("No records found.")
    else:
        for c in courses:
            gp = get_grade_point(c['marks'])
            print(f"{c['name']:<20} | {c['credits']:<8} | {c['marks']:<6} | {gp:<8}")
    print("="*50 + "\n")

def generate_summary(courses):
    sgpa = calculate_sgpa(courses)
    backlogs = check_backlogs(courses)
    
    print("\n" + "#"*30)
    print("   ACADEMIC SUMMARY REPORT")
    print("#"*30)
    print(f"Total Courses: {len(courses)}")
    print(f"Calculated SGPA: {sgpa}")
    
    if backlogs:
        print(f"WARNING: You have backlogs in: {', '.join(backlogs)}")
    else:
        print("Status: All Clear! Good job.")
    print("#"*30 + "\n")