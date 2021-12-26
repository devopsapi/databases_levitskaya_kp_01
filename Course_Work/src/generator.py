import psycopg2
from psycopg2 import Error
import random


class RandomClasses:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.teacher = 0

    def random(self, n):
        res = n
        names = ['Math', 'English', 'Geography', 'History',
                 'PE', 'Ukrainian', 'Literature', 'Sciense', 'Law']
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="yuliya200216",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="school")
            cursor = connection.cursor()
            cursor.execute(
                "DROP TABLE IF EXISTS classes; CREATE TABLE classes(id SERIAL, name text, teacher integer);")
            for i in range(n):
                try:
                    name = names[random.randint(0, len(names) - 1)]
                    cursor.execute(
                        "INSERT INTO classes (name, teacher) VALUES (%s, (SELECT trunc(random() * %s + 1)::int))", [name, n])
                except(Exception, Error) as error:
                    print("Error with PostgreSQL", error)
                    res -= 1
                connection.commit()
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
        print(str(res) + " Entities added.")


class RandomTeachers:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.surname = ""

    def random(self, n):
        res = n
        names = ['Inna', 'Roma', 'Anna', 'Igor', 'Ivan',
                 'Sofia', 'Nina', 'Sergey', 'Nastya', 'Mark']
        surnames = ['Brido', 'Lightman', 'Astrovski', 'Simanenko',
                    'Dolomon', 'Kojolov', 'Toshevich', 'Vikrian', 'Mokio', 'Ramzeski', 'Lodov']
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="yuliya200216",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="school")
            cursor = connection.cursor()
            cursor.execute(
                "DROP TABLE IF EXISTS teachers; CREATE TABLE teachers(id SERIAL, name text, surname text)")
            for i in range(n):
                try:
                    name = names[random.randint(0, len(names) - 1)]
                    surname = surnames[random.randint(0, len(names) - 1)]
                    cursor.execute(
                        "INSERT INTO teachers (name, surname) VALUES (%s, %s)", [name, surname])
                except:
                    res -= 1
                connection.commit()
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
        print(str(res) + " Entities added.")


class RandomGroups:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.year = 0
        self.num_of_exc = 0
        self.teacher = 0

    def random(self, n):
        res = n
        names = ['Math', 'Linguistic', 'History', 'Sciense']
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="yuliya200216",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="school")
            cursor = connection.cursor()
            cursor.execute(
                "DROP TABLE IF EXISTS groups; CREATE TABLE groups(id SERIAL, name text, year integer, num_of_exc integer, teacher integer)")
            for i in range(n):
                try:
                    name = names[random.randint(0, len(names) - 1)]
                    cursor.execute(
                        "INSERT INTO groups (name, year, num_of_exc, teacher) VALUES (%s, (SELECT trunc(random() * 11 + 1)::int), (SELECT trunc(random() * %s + 1)::int), (SELECT trunc(random() * %s + 1)::int))", [name, n, n])
                except:
                    res -= 1
                connection.commit()
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
        print(str(res) + " Entities added.")
