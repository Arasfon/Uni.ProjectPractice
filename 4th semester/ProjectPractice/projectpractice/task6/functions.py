def count_students_by_district_and_beloved_lesson(students, district, beloved_lesson):
    count = 0
    for student in students:
        if student.district == district and student.beloved_lesson == beloved_lesson:
            count += 1
    return count


def count_students_in_the_north_east_district_with_informatics_as_beloved_lesson(students):
    return count_students_by_district_and_beloved_lesson(students, "СВ", "математика")


def average_grade_by_district(students, district):
    grade_sum = 0
    count = 0

    for student in students:
        if student.district == district:
            grade_sum += student.grade
            count += 1

    if count == 0:
        return 0

    return grade_sum / count


def average_grade_in_the_south_district(students):
    return average_grade_by_district(students, "Ю")
