import math


def build_team(persons_number):
    projects_manager_number = 2
    calls_per_month_total_number = 2
    people_in_team_number = 3
    manager_have_people_remains, manager_have_people_whole = math.modf(
        persons_number / projects_manager_number)
    time_have_people = int(manager_have_people_whole)
    kate_have_people = int(manager_have_people_whole)
    tim_one_additional_group_week_1 = ''
    tim_one_additional_group_week_2 = ''
    kate_one_additional_group_week_1 = ''
    kate_one_additional_group_week_2 = ''
    tim_one_extended_group_week_1 = ''
    kate_one_extended_group_week_1 = ''
    tim_one_extended_group_week_2 = ''
    kate_one_extended_group_week_2 = ''

    teams_per_tim_per_day_2_week_whole = 1
    teams_per_tim_per_day_1_week_whole = 2
    teams_per_kate_per_day_2_week_whole=2
    teams_per_kate_per_day_1_week_whole=1

    if manager_have_people_remains == 0.0:
        persons_per_manager_per_day_remains, persons_per_manager_per_day_whole = math.modf(
            persons_number / projects_manager_number / calls_per_month_total_number)
        time_have_people = int(manager_have_people_whole)
        kate_have_people = int(manager_have_people_whole)
        persons_per_tim_per_day_count_1_week = int(persons_per_manager_per_day_whole)
        persons_per_kate_per_day_count_1_week = int(persons_per_manager_per_day_whole)
        persons_per_tim_per_day_count_2_week = int(persons_per_manager_per_day_whole)
        persons_per_kate_per_day_count_2_week = int(persons_per_manager_per_day_whole)





        if persons_per_manager_per_day_remains == 0.0:
            teams_per_manager_per_day_remains, teams_per_manager_per_day_whole = math.modf(
                persons_number / projects_manager_number / calls_per_month_total_number / people_in_team_number)
            if teams_per_manager_per_day_remains == 0.0:
                time_have_people = int(manager_have_people_whole)
                kate_have_people = int(manager_have_people_whole)

                teams_per_tim_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                teams_per_tim_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                teams_per_kate_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                teams_per_kate_per_day_2_week_whole = int(teams_per_manager_per_day_whole)


            else:

                if teams_per_manager_per_day_remains < 0.4:
                    teams_per_manager_per_day_whole=int(teams_per_manager_per_day_whole)
                    time_have_people = int(manager_have_people_whole )
                    kate_have_people = int(manager_have_people_whole )
                    persons_per_tim_per_day_count_1_week = int(persons_per_manager_per_day_whole)
                    persons_per_kate_per_day_count_1_week = int(persons_per_manager_per_day_whole)
                    persons_per_tim_per_day_count_2_week = int(persons_per_manager_per_day_whole)
                    persons_per_kate_per_day_count_2_week = int(persons_per_manager_per_day_whole)
                    teams_per_tim_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_tim_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_kate_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_kate_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                    tim_one_extended_group_week_1 = 1
                    tim_one_extended_group_week_2 = 1
                    kate_one_extended_group_week_1 = 1
                    kate_one_extended_group_week_2 = 1
                else:
                    time_have_people = int(manager_have_people_whole)
                    kate_have_people = int(manager_have_people_whole)
                    persons_per_tim_per_day_count_1_week = int(persons_per_manager_per_day_whole)
                    persons_per_kate_per_day_count_1_week = int(persons_per_manager_per_day_whole)
                    persons_per_tim_per_day_count_2_week = int(persons_per_manager_per_day_whole)
                    persons_per_kate_per_day_count_2_week = int(persons_per_manager_per_day_whole)
                    teams_per_tim_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_tim_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_kate_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_kate_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                    tim_one_additional_group_week_1 = 1
                    tim_one_additional_group_week_2 = 1
                    kate_one_additional_group_week_1 = 1
                    kate_one_additional_group_week_2 = 1
                    teams_per_manager_per_day_whole = round(teams_per_manager_per_day_whole)



        if persons_per_manager_per_day_remains != 0.0:
            time_have_people = int(manager_have_people_whole)
            kate_have_people = int(manager_have_people_whole)
            persons_per_tim_per_day_count_1_week = int(persons_per_manager_per_day_whole)
            persons_per_kate_per_day_count_1_week = int(persons_per_manager_per_day_whole)
            one_week_peroson = int(persons_per_manager_per_day_whole)
            two_week_peroson = one_week_peroson + 1
            persons_per_tim_per_day_count_2_week = int(two_week_peroson)
            persons_per_kate_per_day_count_2_week = int(two_week_peroson)
            teams_per_manager_per_day_remains_1_week, teams_per_manager_per_day_whole = math.modf(
                one_week_peroson / people_in_team_number)
            teams_per_manager_per_day_remains_2_week, teams_per_manager_per_day_whole_2_week = math.modf(
                two_week_peroson / people_in_team_number)
            if one_week_peroson % 3 == 0:
                teams_per_manager_per_day_whole = one_week_peroson//3
                teams_per_tim_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                teams_per_kate_per_day_1_week_whole = int(teams_per_manager_per_day_whole)

            else:
                if teams_per_manager_per_day_remains_1_week < 0.4:
                    teams_per_tim_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_kate_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_manager_per_day_whole = int(teams_per_manager_per_day_whole)
                    tim_one_extended_group_week_1 = 1
                    kate_one_extended_group_week_1 = 1
                else:
                    teams_per_tim_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_kate_per_day_1_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_manager_per_day_whole = round(
                        teams_per_manager_per_day_whole)
                    tim_one_additional_group_week_1 = 1
                    kate_one_additional_group_week_1 = 1
            if two_week_peroson % 3 == 0:
                persons_per_projects_manager_per_day_count_2_week = two_week_peroson // people_in_team_number
                teams_per_tim_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                teams_per_kate_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
            else:
                if teams_per_manager_per_day_remains_2_week < 0.4:
                    teams_per_manager_per_day_whole_2_week = int(
                        teams_per_manager_per_day_whole_2_week)
                    teams_per_tim_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_kate_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                    tim_one_extended_group_week_2 = 1
                    kate_one_extended_group_week_2 = 1
                else:
                    teams_per_manager_per_day_whole_2_week = round(
                        teams_per_manager_per_day_whole_2_week)
                    teams_per_tim_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                    teams_per_kate_per_day_2_week_whole = int(teams_per_manager_per_day_whole)
                    tim_one_additional_group_week_2 = 1
                    kate_one_additional_group_week_2 = 1


    else:
        manager_have_people_count = persons_number / projects_manager_number
        tim_have_people = int(manager_have_people_count)
        kate_have_people = tim_have_people+1
        if tim_have_people % 2 == 0:
            persons_per_tim_per_day_count = tim_have_people // calls_per_month_total_number
            teams_per_tim_per_day_remains, teams_per_tim_per_day_whole = math.modf(
                persons_per_tim_per_day_count / 3)
            persons_per_tim_per_day_count_1_week = int(persons_per_tim_per_day_count)
            persons_per_tim_per_day_count_2_week = int(persons_per_tim_per_day_count)
            if teams_per_tim_per_day_remains == 0.0:
                teams_per_tim_per_day_1_week_whole = int(teams_per_tim_per_day_whole)
                teams_per_tim_per_day_2_week_whole = int(teams_per_tim_per_day_whole)
            else:

                teams_per_tim_per_day_remains, teams_per_tim_per_week_whole = math.modf(
                    persons_per_tim_per_day_count / 3)


                if teams_per_tim_per_day_remains == 0.0:
                    teams_per_tim_per_day_1_week_whole = int(teams_per_tim_per_week_whole)
                else:
                    if teams_per_tim_per_day_remains < 0.4:
                        teams_per_tim_per_day_1_week_whole = int(teams_per_tim_per_week_whole)
                        tim_one_extended_group_week_1 = 1
                        tim_one_extended_group_week_2 = 1
                        teams_per_tim_per_day_2_week_whole = int(teams_per_tim_per_week_whole)
                    else:
                        teams_per_tim_per_day_1_week_whole = round(teams_per_tim_per_week_whole)
                        tim_one_additional_group_week_1 = 1
                        teams_per_tim_per_day_2_week_whole = int(teams_per_tim_per_week_whole)
                        tim_one_additional_group_week_2 = 1



        else:
            persons_per_tim_per_day_count = tim_have_people // calls_per_month_total_number
            one_week_peroson = int(persons_per_tim_per_day_count)
            persons_per_tim_per_day_count_1_week = int(one_week_peroson)
            two_week_peroson = one_week_peroson+1
            persons_per_tim_per_day_count_2_week = int(two_week_peroson)
            teams_per_tim_per_day_1_week_remains, teams_per_tim_per_day_1_week_whole = math.modf(
                one_week_peroson / 3)
            teams_per_tim_per_day_2_week_remains, teams_per_tim_per_day_2_week_whole = math.modf(
                two_week_peroson / 3)

            if teams_per_tim_per_day_1_week_remains == 0.0:
                teams_per_tim_per_day_1_week_whole = int(teams_per_tim_per_day_1_week_whole)
            else:
                if teams_per_tim_per_day_1_week_remains < 0.4:
                    teams_per_tim_per_day_1_week_whole = int(teams_per_tim_per_day_1_week_whole)
                    tim_one_extended_group_week_1 = 1
                    teams_per_tim_per_day_whole=int(teams_per_tim_per_day_1_week_whole)
                else:
                    teams_per_tim_per_day_1_week_whole = int(teams_per_tim_per_day_1_week_whole)
                    tim_one_additional_group_week_1 = 1


            if teams_per_tim_per_day_2_week_remains == 0.0:
                teams_per_tim_per_day_2_week_whole=int(teams_per_tim_per_day_2_week_whole)

            else:
                if teams_per_tim_per_day_2_week_remains < 0.4:
                    teams_per_tim_per_day_2_week_whole=int(teams_per_tim_per_day_2_week_whole)

                else:
                    teams_per_tim_per_day_2_week_whole = round(teams_per_tim_per_day_2_week_whole)
                    tim_one_additional_group_week_1 = 1




        if kate_have_people % 2 == 0:
            persons_per_kate_per_day_count = kate_have_people // calls_per_month_total_number
            persons_per_kate_per_day_count_1_week = persons_per_kate_per_day_count
            persons_per_kate_per_day_count_2_week = persons_per_kate_per_day_count
            teams_per_kate_per_day_remains, teams_per_kate_per_day_whole = math.modf(
                persons_per_kate_per_day_count / 3)
            if teams_per_kate_per_day_remains == 0.0:
                teams_per_kate_per_day_1_week_whole = int(teams_per_kate_per_day_whole)

            else:
                if teams_per_kate_per_day_remains < 0.4:
                    teams_per_kate_per_day_whole=int(teams_per_kate_per_day_whole)
                    teams_per_kate_per_day_1_week_whole = int(teams_per_kate_per_day_whole)
                    teams_per_kate_per_day_2_week_whole = int(teams_per_kate_per_day_whole)
                    kate_one_extended_group_week_1 = 1
                    kate_one_extended_group_week_2 =1
                else:
                    kate_one_additional_group_week_1 = 1
                    kate_one_additional_group_week_2 = 1
                    teams_per_kate_per_day_1_week_whole = int(teams_per_kate_per_day_whole)
                    teams_per_kate_per_day_2_week_whole = int(teams_per_kate_per_day_whole)
                    teams_per_kate_per_day_whole = round(teams_per_kate_per_day_whole)



        else:
            persons_per_kate_per_day_count = kate_have_people // calls_per_month_total_number
            one_week_peroson = int(persons_per_kate_per_day_count)
            two_week_peroson = one_week_peroson+1
            persons_per_kate_per_day_count_1_week = int(one_week_peroson)
            persons_per_kate_per_day_count_2_week = two_week_peroson

            teams_per_kate_per_day_1_week_remains, teams_per_kate_per_day_1_week_whole = math.modf(
                one_week_peroson / 3)
            teams_per_kate_per_day_2_week_remains, teams_per_kate_per_day_2_week_whole = math.modf(
                two_week_peroson / 3)

            if teams_per_kate_per_day_1_week_remains == 0.0:
                teams_per_kate_per_day_1_week_whole = int(one_week_peroson)

            else:
                if teams_per_kate_per_day_1_week_remains < 0.4:
                    teams_per_kate_per_day_1_week_whole = int(teams_per_kate_per_day_1_week_whole)
                    kate_one_extended_group_week_1 = 1
                else:
                    teams_per_kate_per_day_1_week_whole = int(teams_per_kate_per_day_1_week_whole)
                    kate_one_additional_group_week_1 = 1



            if teams_per_kate_per_day_2_week_remains == 0.0:
                teams_per_kate_per_day_2_week_whole = int(
                    teams_per_kate_per_day_2_week_whole)

            else:
                if teams_per_kate_per_day_2_week_remains < 0.4:
                    kate_one_extended_group_week_2 = 1

                else:
                    kate_one_additional_group_week_2 = 1


    commands = {
        'tim': {
            'tim_all_student': time_have_people,
            'tim_week_1': persons_per_tim_per_day_count_1_week,
            'tim_week_2': persons_per_tim_per_day_count_2_week,
            'tim_group_1': teams_per_tim_per_day_1_week_whole,
            'tim_group_2': teams_per_tim_per_day_2_week_whole,
            'tim_one_additional_group_week_1': tim_one_additional_group_week_1,
            'tim_one_extended_group_week_1': tim_one_extended_group_week_1,
            'tim_one_additional_group_week_2': tim_one_additional_group_week_2,
            'tim_one_extended_group_week_2': tim_one_extended_group_week_2},
        'kate': {'kate_all_student': kate_have_people,
                 'kate_week_1': persons_per_kate_per_day_count_1_week,
                 'kate_week_2': persons_per_kate_per_day_count_2_week,
                 'kate_group_1': teams_per_kate_per_day_1_week_whole,
                 'kate_group_2': teams_per_kate_per_day_2_week_whole,
                 'kate_one_additional_group_week_1': kate_one_additional_group_week_1,
                 'kate_one_extended_group_week_1': kate_one_extended_group_week_1,
                 'kate_one_additional_group_week_2': kate_one_additional_group_week_2,
                 'kate_one_extended_group_week_2': kate_one_extended_group_week_2}
    }
    return commands

