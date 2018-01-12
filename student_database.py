# -*- encoding:utf-8 -*-
# __author__=='Gan'

import random
import string

import pymysql


class Student:
    def __init__(self, letters):
        self.letters = list(letters)
        self.brith_years = ['1997/', '1996/', '1995/']
        self.create_years = ['2007/', '2010/', '2012/']
        self.generate_random()

    def generate_random(self):
        self.username = ''.join(random.choice(self.letters) for _ in range(5))
        self.password = ''.join(random.choice(self.letters) for _ in range(5))
        self.birth_date = random.choice(self.brith_years) + '02/02'
        self.create_date = random.choice(self.create_years) + '02/02'
        self.gender = random.randint(0, 1)


def insert_random_data(student):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='student')
    cur = conn.cursor()
    insert_sql = "INSERT INTO student (id, username, password, birth_date, gender, create_date) " \
                 "VALUES (NULL, '{s.username}', '{s.password}', '{s.birth_date}', {s.gender}, '{s.create_date}')".format(s=student)
    cur.execute(insert_sql)
    conn.commit()
    cur.close()
    conn.close()

def main():
    letters = string.ascii_lowercase
    student = Student(letters)
    insert_random_data(student)


if __name__ == '__main__':
    [main() for _ in range(100)]