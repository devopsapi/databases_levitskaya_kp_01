import psycopg2
from timeit import default_timer as timer
from psycopg2 import Error
import datetime


class pupils:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.surname = ""
        self.birthday = datetime.date
        self.phoneNumber = 0
        self.address = ""
        self.class_id = 0

    def create(self, id, name, surname, birthday, phoneNumber, address):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO pupils (id, name, surname, birthday, phoneNumber, address) VALUES (%s, %s, %s, %s, %s, %s)"""
            item_tuple = (id, name, surname, birthday, phoneNumber, address)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            select_query = """SELECT * from pupils WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, name, surname, birthday, phoneNumber, address):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            update_query = """Update pupils 
                                SET name = (%s),
                                    surname = (%s),
                                    birthday = (%s),
                                    phoneNumber = (%s)
                                    address = (%s)
                                WHERE id = %s"""
            item_tuple = (name, surname, birthday, phoneNumber, address, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity updated")

        except (Exception, Error) as error:
            print("Error occured in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            cursor.execute("Delete from pupils WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, genNum):

        if (genNum < 0):
            print('Error with input!')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()

            generate_query = """INSERT INTO pupils (name, surname, birthday, phoneNumber, address)
                                    SELECT md5(random()::text), md5(random()::text)
                                    FROM generate_series(1, %s)"""
            item_tuple = genNum,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Entity generated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def searchPupilClass(self, name, surname, phoneNumber):

        sttime = timer()

        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            select_query = """ SELECT name, surname, phoneNumber  
                               FROM pupils, classes
                               WHERE name LIKE %s AND surname LIKE %s AND phoneNumber LIKE %s AND pupil.class_id = class.id
                               ORDER BY rating DESC"""
            item_tuple = (name, '%' + surname + '%', '%' + phoneNumber + '%')
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
            error()
        finally:
            if connection:
                cursor.close()
                connection.close()

                endtime = timer()

                print("Search operation take " + str((endtime - sttime) * 1000) + " ms")


class shoolClasses:

    def __init__(self):
        self.id = 0
        self.teacher_id = 0

    def create(self, id, teacher_id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO classes (id, teacher_id) VALUES (%s, %s)"""
            item_tuple = (id, teacher_id)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            select_query = """SELECT * from classes WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, teacher_id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            update_query = """Update pupils 
                              SET teacher_id = (%s)
                               WHERE id = (%s)"""
            item_tuple = (teacher_id, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity updated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            cursor.execute("Delete from classes WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, genNum):

        if (genNum < 0):
            print('Error with input!')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()

            generate_query = """INSERT INTO classes (teacher_id)
                                SELECT md5(random()::text), (trunc(random()*10)::int), (floor(random()*((SELECT id FROM teachers ORDER BY id DESC LIMIT 1) - (SELECT id FROM teachers ORDER BY id LIMIT 1) + 1) + (SELECT id FROM teachers ORDER BY id LIMIT 1))::int), (trunc(random()*(SELECT id FROM teachers ORDER BY id DESC LIMIT 1))::int)
                                FROM generate_series(1, %s)"""
            item_tuple = genNum,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Entity generated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


class teachers:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.surname = ""
        self.isAClassroomTeacher = 0

    def create(self, id, name, surname, isAClassroomTeacher):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO teachers (id, name, surname, isAClassroomTeacher)) VALUES (%s, %s, %s, %s)"""
            item_tuple = (id, name, surname, isAClassroomTeacher)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            select_query = """SELECT * from teachers WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, name, surname, isAClassroomTeacher):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            update_query = """Update teachers 
                                  SET teacher_id = (%s),
                                      name = (%s), 
                                      surname = (%s), 
                                      isAClassroomTeacher = (%s)
                                   WHERE id = (%s)"""
            item_tuple = (name, surname, isAClassroomTeacher, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity updated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            cursor.execute("Delete from teachers WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, genNum):

        if (genNum < 0):
            print('Error with input!')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()

            generate_query = """INSERT INTO teachers (id)
                                    SELECT md5(random()::text), (trunc(random()*10)::int), (floor(random()*((SELECT id FROM teachers ORDER BY id DESC LIMIT 1) - (SELECT id FROM teachers ORDER BY id LIMIT 1) + 1) + (SELECT id FROM teachers ORDER BY id LIMIT 1))::int), (trunc(random()*(SELECT id FROM teachers ORDER BY id DESC LIMIT 1))::int)
                                    FROM generate_series(1, %s)"""
            item_tuple = genNum,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Entity generated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


class timetables:

    def __init__(self):
        self.id = 0
        self.lessonNumber = 0
        self.day = datetime.date
        self.subject_id = 0
        self.teacher_id = 0
        self.class_id = 0

    def create(self, id, lessonNumber, day, subject_id, teacher_id, class_id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO timetable (id, lessonNumber, day, subject_id, teacher_id, class_id) VALUES (%s, %s, %s, %s, %s, %s)"""
            item_tuple = (id, lessonNumber, day, subject_id, teacher_id, class_id)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            select_query = """SELECT * from timetable WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, lessonNumber, day, subject_id, teacher_id, class_id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            update_query = """Update timetable 
                                  SET lessonNumber = (%s),
                                      day = (%s),
                                      teacher_id = (%s),
                                      teacher_id = (%s),
                                      class_id = (%s),
                                      isAClassroomTeacher = (%s)
                                   WHERE id = (%s)"""
            item_tuple = (lessonNumber, day, subject_id, teacher_id, class_id, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity updated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            cursor.execute("Delete from timetable WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, genNum):

        if (genNum < 0):
            print('Error with input!')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()

            generate_query = """INSERT INTO timetable (id)
                                    SELECT md5(random()::text), (trunc(random()*10)::int), (floor(random()*((SELECT id FROM teachers ORDER BY id DESC LIMIT 1) - (SELECT id FROM teachers ORDER BY id LIMIT 1) + 1) + (SELECT id FROM teachers ORDER BY id LIMIT 1))::int), (trunc(random()*(SELECT id FROM subjects ORDER BY id DESC LIMIT 1))::int)
                                    FROM generate_series(1, %s)"""
            item_tuple = genNum,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Entity generated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


class subjects:

    def __init__(self):
        self.id = 0
        self.title = 0
        self.credit = 0

    def create(self, id, title, credit):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO subjects (id, title, credit) VALUES (%s, %s, %s)"""
            item_tuple = (id, title, credit)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            select_query = """SELECT * from subjects WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(select_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, id, title, credit):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            update_query = """Update subjects 
                                  SET title  = (%s),
                                      credit = (%s),
                                   WHERE id = (%s)"""
            item_tuple = (title, credit, id)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity updated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self, id):

        if (id < 1):
            print('Invalid id entered')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()
            cursor.execute("Delete from subjects WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def generate(self, genNum):

        if (genNum < 0):
            print('Error with input!')
            return
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="1337",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="library_db")
            cursor = connection.cursor()

            generate_query = """INSERT INTO subjects (id)
                                    SELECT md5(random()::text)
                                    FROM generate_series(1, %s)"""
            item_tuple = genNum,
            cursor.execute(generate_query, item_tuple)
            connection.commit()

            count = cursor.rowcount
            print(count, "Entity generated")

        except (Exception, Error) as error:
            print("Error occurred in PostgreSQL: ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
