import pymysql

db = pymysql.connect(host='localhost', user='root', password='root123', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute('CREATE DATABASE spiders DEFAULT CREATE CHARACTER SET utf8mb4')
db.close()

db = pymysql.connect(host='localhost', user='root', password='root123', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'
cursor.execute(sql)
# db.close()

# 插入数据
id = '20220001'
user = 'Easy'
age = 20
sql = 'INSERT INTO students(id,name,age) VALUES (%s,%s,%s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
# db.close()


# 动态构造 sql语句
data = {
    'id': '20230001',
    'name:': 'Easy',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Faild')
    db.rollback()
# db.close()


# 更灵活的方法 去重 如果重复 update 如果没有 新加
data = {
    'id': '20230001',
    'name:': 'Easy',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys,
                                                                                      values=values)
update = ','.join(["{key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('Successful')
        db.commit()
except:
    print("Failed")
    db.rollback()
# db.close()

# delete
condition = 'age>20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# select
sql = 'SELECT * FROM students WHERE age>20'
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one = cursor.fetchone()
    print('One:',one)
    results = cursor.fetchall()
    print('results:',results)
    print('Results type', type(results))
    for row in results:
        print(row)

    # row = cursor.fetchone()
    # while row:
    #     print('Row:',row)
    #     row = cursor.fetchone()
except:
    print('Error')


