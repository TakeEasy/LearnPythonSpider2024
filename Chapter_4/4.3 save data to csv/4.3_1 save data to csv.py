import csv

with open('data.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer = csv.writer(csvfile, delimiter=' ')  # 设置分隔符
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10001', 'Bob', 22])
    writer.writerow([['10001', 'Mike', 20], ['10001', 'Mike', 20], ['10001', 'Mike', 20]])

    fieldnames = ['id', 'name', 'age']
    writer2 = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer2.writerow({'id': '10002', 'name': 'Mark', 'age': 22})

with open('data.csv', 'r', encoding='utf-8'):
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
