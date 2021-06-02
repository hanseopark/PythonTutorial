import pymysql
import pandas as pd

class_db = pymysql.connect(
    user='root',
    passwd='0000',
    host='127.0.0.1',
    db='class',
    charset='utf8mb4'
)

cursor = class_db.cursor(pymysql.cursors.DictCursor)
#cursor = class_db.cursor()

sql = "select * from `student`;"
cursor.execute(sql)
result = cursor.fetchall()
result = pd.DataFrame(result)
print(result)
