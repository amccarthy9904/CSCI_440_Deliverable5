import pymysql

class Query:

    def __init__(self):
        self.query1 = ''
        self.query2 = ''
        self.query3 = ''
        self.query4 = ''
        self.query5 = ''
        self.result1 = ''
        self.result2 = ''
        self.result3 = ''
        self.result4 = ''
        self.result5 = ''

    def run_queries(self):
        connection = pymysql.connect(host='localhost', user='', passwd ='' db='')
        cursor = connection.cursor
        cursor.execute(self.query1)
        self.result1 = cursor.fetchall()
        cursor.execute(self.query2)
        self.result2 = cursor.fetchall()
        cursor.execute(self.query3)
        self.result3 = cursor.fetchall()
        cursor.execute(self.query4)
        self.result4 = cursor.fetchall()
        cursor.execute(self.query5)
        self.result5 = cursor.fetchall()

        return [self.result1, self.result2, self.result3, self.result4, self.result5]
