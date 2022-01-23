from random import randint




def chunks_generators(students, chunks_number):
    for student in range(0, len(students), chunks_number):
        yield students[student: student + chunks_number]



def distribution_students(one_additional_group, one_extended_group, week ):
    formed_group = {}

    if one_additional_group:
        additional_group = week[:2]
        additional_group = list(chunks_generators(additional_group, 2))
        for group in additional_group:
            name_additional_group = randint(1, 999)
            formed_group.update({name_additional_group: group})

        remained_students = week[2:]
        created_goups = list(chunks_generators(remained_students, 3))
        for group in created_goups:
            name_group = randint(1, 999)
            formed_group.update({name_group: group})


    if one_extended_group:
        firs_id = week[:1]
        remained_students = week[1:]
        created_goups = list(chunks_generators(remained_students, 3))
        created_goups[0].append(*firs_id)

        for group in created_goups:
            name_group = randint(1, 999)
            formed_group.update({name_group: group})


    if not one_extended_group and not one_additional_group:
        created_goups = list(chunks_generators(week, 3))
        for group in created_goups:
            name_group = randint(1, 999)
            formed_group.update({name_group: group})
    return formed_group



