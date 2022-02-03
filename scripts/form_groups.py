import copy

from random import randint



def chunks_generators(students, chunks_number):
    for student in range(0, len(students), chunks_number):
        yield students[student: student + chunks_number]


def distribute_students(students):
    week_1_students_number = len(students) // 2
    week_1_students = students[:week_1_students_number]
    tim_week_1_students_number = week_1_students_number // 2
    tim_week_1_students = students[:tim_week_1_students_number]
    kate_week_1_students = students[tim_week_1_students_number:week_1_students_number]
    week_2_students = students[week_1_students_number:]
    kate_week_2_students_number = len(week_2_students) // 2
    kate_week_2_students = week_2_students[:kate_week_2_students_number]
    tim_week_2_students = week_2_students[kate_week_2_students_number:]
    return tim_week_1_students, kate_week_1_students, kate_week_2_students, tim_week_2_students


def add_unique_number(students_groups):
    named_groups = {}
    for group in students_groups:
        group_name = randint(1, 333)
        named_groups.update({group_name: group})
    return named_groups


def form_groups(distributed_students):
    """Forms groups, the total number of people should not be less than 8."""

    generated_groups = list(chunks_generators(distributed_students, 3))
    groups = copy.deepcopy(generated_groups)

    if len(groups[-1]) == 1:
        united_two_last_groups = groups[-1] + groups[-2]
        groups = groups[:-2]
        groups.append(united_two_last_groups)
        unique_groups = add_unique_number(groups)
        return unique_groups
    else:
        unique_groups = add_unique_number(groups)
        return unique_groups
