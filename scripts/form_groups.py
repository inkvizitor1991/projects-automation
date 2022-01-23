from scripts.build_team import build_team
from scripts.distribution_students import distribution_students





def form_gorups(group):
    students_number = len(group)
    commands = build_team(students_number)
    tim_all_student_1_week = group[:commands['tim']['tim_week_1']]
    len_tim_all_student_1_week = len(tim_all_student_1_week)

    tim_one_additional_group_week_1 = commands['tim']['tim_one_additional_group_week_1']
    tim_one_extended_group_week_1 = commands['tim']['tim_one_extended_group_week_1']
    tim_one_additional_group_week_2 = commands['tim']['tim_one_additional_group_week_2']
    tim_one_extended_group_week_2 = commands['tim']['tim_one_extended_group_week_2']
    tim_all_student_2_week = group[len_tim_all_student_1_week : commands['tim']['tim_all_student']]
    kate_all_student_1_week = group[commands['tim']['tim_all_student']: commands['tim']['tim_all_student']+commands['kate']['kate_week_1']]
    len_kate_all_student_1_week = int(commands['tim']['tim_all_student']+commands['kate']['kate_week_1'])
    kate_all_student_2_week = group[len_kate_all_student_1_week:]
    kate_one_additional_group_week_1 = commands['kate']['kate_one_additional_group_week_1']
    kate_one_extended_group_week_1 = commands['kate']['kate_one_extended_group_week_1']

    kate_one_additional_group_week_2 = commands['kate']['kate_one_additional_group_week_2']
    kate_one_extended_group_week_2 = commands['kate']['kate_one_extended_group_week_2']

    groups_for_tim_week_2 = distribution_students(tim_one_additional_group_week_2, tim_one_extended_group_week_2, tim_all_student_2_week)
    groups_for_tim_week_1 = distribution_students(tim_one_additional_group_week_1, tim_one_extended_group_week_1, tim_all_student_1_week)

    groups_for_kate_week_1 = distribution_students(kate_one_additional_group_week_1, kate_one_extended_group_week_1, kate_all_student_1_week)
    groups_for_kate_week_2 = distribution_students(kate_one_additional_group_week_2, kate_one_extended_group_week_2, kate_all_student_2_week)
    formed_groups = {'groups_for_tim_week_1':groups_for_tim_week_1,
                     'groups_for_tim_week_2':groups_for_tim_week_2,
                     'groups_for_kate_week_1':groups_for_kate_week_1,
                     'groups_for_kate_week_2':groups_for_kate_week_2
                     }
    return formed_groups




