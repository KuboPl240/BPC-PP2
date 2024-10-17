
students = {
    "Alice": [("Math", 4), ("Science", 5), ("English", 3)],
    "Bob": [("Math", 2), ("Science", 1), ("English", 3)],
    "Charlie": [("Math", 5), ("Science", 5), ("English", 4)]
}


def convert_to_courses(students):
    courses = {}
    for student_name, course_list in students.items():
        for course_name, evaluation in course_list:
            if course_name not in courses:
                courses[course_name] = []
            courses[course_name].append((student_name, evaluation))
    return courses


def average_evaluation_in_course(course_name, courses):
    course_evaluations = courses.get(course_name, [])
    total_score = sum([evaluation for student_name, evaluation in course_evaluations])
    return total_score / len(course_evaluations)


def best_course(courses):
    best_course = None
    best_avg = float('inf')
    for course_name in courses:
        avg = average_evaluation_in_course(course_name, courses)
        if avg < best_avg:
            best_avg_avg = avg
            best_course = course_name
    return best_course


def sort_courses(courses):
    return sorted(courses.keys(), key=lambda course: average_evaluation_in_course(course, courses))


courses = convert_to_courses(students)
print("Courses dictionary:", courses)
print("Average evaluation in Math:", average_evaluation_in_course("Math", courses))
print("Best course:", best_course(courses))
print("Courses sorted by average evaluation:", sort_courses(courses))
