from scripts.form_groups import form_groups, distribute_students
from automation.models import (
    Project, Student,
    ProjectManager, Command,
    ParticipantProject
)

students = Student.objects.filter(category__name='Джуниор')
students_new = Student.objects.filter(category__name='Новичек')
students_new_3 = Student.objects.filter(category__name='Новичек +3')

students_junior = []
new_students = []

for student in students:
    students_junior.append(student.id)

for student in students_new:
    new_students.append(student.id)

for student in students_new_3:
    new_students.append(student.id)


def create_groups(pm_name, groups, project_name):
    for commands in groups:
        project = Project.objects.filter(name=project_name).first()
        command = Command(command_name=commands, project=project)
        command.save()
        for students in groups[commands]:
            pm = ProjectManager.objects.filter(first_name=pm_name).first()
            student = Student.objects.filter(id=students).first()
            ParticipantProject.objects.create(
                student=student,
                project_manager=pm,
                command=command
            )


tim_week_1_students_junior, kate_week_1_students_junior, kate_week_2_students_junior, tim_week_2_students_junior = distribute_students(
    students_junior)
tim_week_1_students_beginner, kate_week_1_students_beginner, kate_week_2_students_beginner, tim_week_2_students_beginner = distribute_students(
    new_students)

junior_groups_for_tim_week_1 = form_groups(tim_week_1_students_junior)
junior_groups_for_kate_week_1 = form_groups(kate_week_1_students_junior)
junior_groups_for_kate_week_2 = form_groups(kate_week_2_students_junior)
junior_groups_for_tim_week_2 = form_groups(tim_week_2_students_junior)

beginner_groups_for_tim_week_2 = form_groups(tim_week_1_students_beginner)
beginner_groups_for_tim_week_1 = form_groups(kate_week_1_students_beginner)
beginner_groups_for_kate_week_2 = form_groups(kate_week_2_students_beginner)
beginner_groups_for_kate_week_1 = form_groups(tim_week_2_students_beginner)



