from data import Student


def read_one_student_from_stdin():
    district = input("Введите округ: ").upper()
    last_name = input("Введите фамилию: ")
    beloved_lesson = input("Введите любимый предмет: ").lower()
    grade = int(input("Введите балл: "))

    student = Student()

    student.district = district
    student.last_name = last_name
    student.beloved_lesson = beloved_lesson
    student.grade = grade

    return student


def read_students_from_stdin(count):
    students = []
    for i in range(count):
        print(f"Введите данные {i + 1} ученика:")
        students.append(read_one_student_from_stdin())
    return students
