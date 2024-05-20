from functions import average_grade_in_the_south_district, count_students_in_the_north_east_district_with_informatics_as_beloved_lesson
from input import read_students_from_stdin

print('Данная программа считает количество учеников в Северо-Восточном округе с любимым предметом "математика", '
      + 'а также Средний балл учеников в Южном округе.')

student_count = int(input("Введите количество учеников: "))
students = read_students_from_stdin(student_count)

count_of_students_in_the_north_east_district_with_informatics_as_beloved_lesson = (
    count_students_in_the_north_east_district_with_informatics_as_beloved_lesson(students)
)
average_grade_in_the_south_district_value = average_grade_in_the_south_district(students)

print(
    'Количество учеников в Северо-Восточном округе с любимым предметом "математика":',
    count_of_students_in_the_north_east_district_with_informatics_as_beloved_lesson,
)
print(f"Средний балл учеников в Южном округе: {average_grade_in_the_south_district_value}")
