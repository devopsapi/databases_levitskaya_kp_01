from model import pupils
from model import teachers
from model import subjects
from model import timetables
from model import shoolClasses
from view import view

v = view()
pupil = pupils()
teacher = teachers()
subject = subjects()
timetable = timetables()
schoolClass = shoolClasses()

command = view.readCommand()

if (command == 'create'):

    table = view.readTable()

    if (table == 'pupils'):
        id = view.getInt()
        name = view.getVal()
        surname = view.getVal()
        birthday = view.getVal()
        phoneNumber = view.getVal()
        address = view.getVal()
        class_id = view.getVal()
        pupil.create(id, name, surname, birthday, phoneNumber, address, class_id)
    elif (table == 'teachers'):
        id = view.getInt()
        name = view.getVal()
        surname = view.getVal()
        isAClassroomTeacher = view.getVal()
        teacher.create(id, name, surname, isAClassroomTeacher)
    elif (table == 'subject'):
        id = view.getInt()
        title = view.getVal()
        credit = view.getInt()
        subject.create(id, title, credit)
    elif (table == 'schoolClasses'):
        id = view.getInt()
        teacher_id = view.getInt()
        schoolClass.create(id, teacher_id)
    elif (table == 'timetables'):
        id = view.getInt()
        lessonNumber = view.getVal()
        day = view.getVal()
        subject_id = view.getVal()
        teacher_id = view.getVal()
        class_id = view.getVal()
        timetable.create(id, lessonNumber, day, subject_id, teacher_id, class_id)
    else:
        print('Table with that name does not exist')

elif (command == 'read'):

    table = view.readTable()

    if (table == 'pupils'):
        id = view.getInt()
        pupil.read(id)
    elif (table == 'teachers'):
        id = view.getInt()
        teacher.read(id)
    elif (table == 'subjects'):
        id = view.getInt()
        subject.read(id)
    elif (table == 'schoolClasses'):
        id = view.getInt()
        schoolClass.read(id)
    elif (table == 'timetables'):
        id = view.getInt()
        timetable.read(id)
    else:
        print('Table with that name does not exist')

elif (command == 'update'):

    table = view.readTable()

    if (table == 'pupils'):
        id = view.getInt()
        name = view.getVal()
        surname = view.getVal()
        birthday = view.getVal()
        phoneNumber = view.getVal()
        address = view.getVal()
        class_id = view.getVal()
        pupil.update(id, name, surname, birthday, phoneNumber, address, class_id)
    elif (table == 'teachers'):
        id = view.getInt()
        name = view.getVal()
        surname = view.getVal()
        isAClassroomTeacher = view.getVal()
        teacher.update(id, name, surname, isAClassroomTeacher)
    elif (table == 'subjects'):
        id = view.getInt()
        title = view.getVal()
        credit = view.getInt()
        subject.update(id, title, credit)
    elif (table == 'schoolClasses'):
        id = view.getInt()
        teacher_id = view.getInt()
        schoolClass.update(id, teacher_id)
    elif (table == 'timetables'):
        id = view.getInt()
        lessonNumber = view.getVal()
        day = view.getVal()
        subject_id = view.getVal()
        teacher_id = view.getVal()
        class_id = view.getVal()
        timetable.update(id, lessonNumber, day, subject_id, teacher_id, class_id)
    else:
        print('Table with that name does not exist')

elif (command == 'delete'):

    table = view.readTable()

    if (table == 'pupils'):
        id = view.getInt()
        pupil.delete(id)
    elif (table == 'teachers'):
        id = view.getInt()
        teacher.delete(id)
    elif (table == 'subjects'):
        id = view.getInt()
        subject.delete(id)
    elif (table == 'schoolClasses'):
        id = view.getInt()
        schoolClass.delete(id)
    elif (table == 'timetables'):
        id = view.getInt()
        timetable.delete(id)
    else:
        print('Table with that name does not exist')

elif (command == 'generate'):

    table = view.readTable()

    if (table == 'pupils'):
        genNum = view.getInt()
        pupil.generate(genNum)
    elif (table == 'teachers'):
        genNum = view.getInt()
        teacher.generate(genNum)
    elif (table == 'subjects'):
        genNum = view.getInt()
        subject.generate(genNum)
    elif (table == 'schoolClasses'):
        genNum = view.getInt()
        schoolClass.generate(genNum)
    elif (table == 'timetables'):
        genNum = view.getInt()
        timetable.generate(genNum)
    else:
        print('Table with that name does not exist')

elif (command == 'search'):

    phoneNumber = view.getInt()
    name = view.getVal()
    surname = view.getVal()

    pupil.searchPupilClass(name, surname, phoneNumber)

else:
    print('Incorrect command')
