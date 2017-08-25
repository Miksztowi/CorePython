# -*- coding:utf-8 -*-
__author__ = "ganbin"
import MySQLdb

if __name__ == '__main__':
    connect = MySQLdb.connect(user='root', password='', db='automotive')
    cursor = connect.cursor()
    cursor.execute('SELECT id, make, model, submodel, year FROM automotive.car_features4')
    cars_1 = cursor.fetchall()
    cursor.execute('SELECT id, make, model, submodel, year FROM automotive.edmunds_cars')
    cars_2 = cursor.fetchall()
    ids_1 = set([x[0] for x in cars_1])
    ids_2 = set([x[0] for x in cars_2])
    difference_ids = ids_1.difference(ids_2)
    print(difference_ids)
    for car in cars_1:
        if car[0] in difference_ids:
            sql = 'INSERT INTO automotive.edmunds_cars(id, make, model, submodel, year)' \
                  'VALUE (%s, %s, %s, %s, %s)'
            cursor.execute(sql, car)
            connect.commit()



