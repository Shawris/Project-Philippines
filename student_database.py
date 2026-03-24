#This is a simple program that calculates within a certain student database
#It acts by looking for specific students by name and locating their specific course
def add_student(students, name):
    if name not in students:
        students[name] = []

#If the person does not exist within the database, it returns as follows
def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
#If the student's name does exist in the database, it prints out how far they have progressed with their specific courses and later prints out their average grade
    courses = students[name]
    print(f"{name}:")
    
    if not courses:
        print(" no completed courses")
    else:
        print(f" {len(courses)} completed courses:")
        total_grade = 0
        for course_name, grade in courses:
            print(f"  {course_name} {grade}")
            total_grade += grade
        print(f" average grade {total_grade / len(courses)}")

def add_course(students: dict, name: str, course: tuple):
    course_name, grade = course
    
    if grade == 0:
        return
    
    if name in students:
        existing_courses = students[name]

        for i in range(len(existing_courses)):
            if existing_courses[i][0] == course_name:
                if grade > existing_courses[i][1]:
                    existing_courses[i] = (course_name, grade)
                return
        
        existing_courses.append(course)

def summary(students: dict):
    print(f"students {len(students)}")
    
    most_courses_count = -1
    best_student_name = ""
    
    best_avg_grade = -1
    best_avg_student_name = ""
    
    for name, courses in students.items():
        if len(courses) > most_courses_count:
            most_courses_count = len(courses)
            best_student_name = name
            
        if courses:
            avg = sum(course[1] for course in courses) / len(courses)
            if avg > best_avg_grade:
                best_avg_grade = avg
                best_avg_student_name = name
                
    print(f"most courses completed {most_courses_count} {best_student_name}")
    print(f"best average grade {best_avg_grade} {best_avg_student_name}")
