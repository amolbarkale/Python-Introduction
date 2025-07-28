class Course:
    total_enrollments = 0

    def __init__(self, course_id, name, instructor, credits, max_capacity):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.credits = credits
        self.max_capacity = max_capacity
        self.enrollments = []  # list of student_ids
        self.grades = {}  # student_id -> grade
        self.waitlist = []

    def __str__(self):
        return f"{self.name} ({self.course_id})"

    def get_available_spots(self):
        return self.max_capacity - len(self.enrollments)

    def get_enrollment_count(self):
        return len(self.enrollments)

    def enroll_student(self, student):
        if student.student_id in self.enrollments:
            return f"{student.name} is already enrolled."

        if len(self.enrollments) < self.max_capacity:
            self.enrollments.append(student.student_id)
            Course.total_enrollments += 1
            return "Enrollment successful"
        else:
            self.waitlist.append(student.student_id)
            return "Added to waitlist"

    def add_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_course_statistics(self):
        grades = list(self.grades.values())
        if not grades:
            return {"average": 0, "highest": 0, "lowest": 0}
        return {
            "average": round(sum(grades) / len(grades), 2),
            "highest": max(grades),
            "lowest": min(grades)
        }

    def is_full(self):
        return len(self.enrollments) >= self.max_capacity

    @classmethod
    def get_total_enrollments(cls):
        return cls.total_enrollments


class Student:
    all_students = []
    total_credits = {}
    total_grades = {}

    def __init__(self, student_id, name, email, program):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.program = program
        self.enrollments = []  # list of Course objects
        self.transcript = {}  # course_id -> grade

        Student.all_students.append(self)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    def enroll_in_course(self, course):
        result = course.enroll_student(self)
        if result.startswith("Enrollment"):
            self.enrollments.append(course)
        return result

    def add_grade(self, course_id, grade):
        self.transcript[course_id] = grade

    def calculate_gpa(self):
        if not self.transcript:
