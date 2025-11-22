def get_grade_point(marks):
    """Converts marks (0-100) to Grade Point (S system generic example)."""
    if marks >= 90: return 10
    elif marks >= 80: return 9
    elif marks >= 70: return 8
    elif marks >= 60: return 7
    elif marks >= 50: return 6
    elif marks >= 40: return 5 # Pass
    else: return 0 # Fail

def calculate_sgpa(courses):
    """Calculates SGPA based on weighted average."""
    total_credits = 0
    total_points = 0
    
    for course in courses:
        credits = course['credits']
        marks = course['marks']
        gp = get_grade_point(marks)
        
        total_credits += credits
        total_points += (credits * gp)
        
    if total_credits == 0:
        return 0.0
    
    return round(total_points / total_credits, 2)

def check_backlogs(courses):
    """Returns a list of courses where the student failed (Marks < 40)."""
    failed_courses = []
    for course in courses:
        if course['marks'] < 40:
            failed_courses.append(course['name'])
    return failed_courses