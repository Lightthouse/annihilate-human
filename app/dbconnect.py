import psycopg2
import settings
from contextlib import closing


class DbConnection:

    def __init__(self):
        self.host = settings.host
        self.user = settings.user
        self.password = settings.password
        self.dbname = settings.dbname
        self.table_name = settings.table_name

    def destroy_man(self, phone):
        phone = self.morph_phone(phone)
        sql_request = f'DELETE * FROM {self.table_name} WHERE phone LIKE (\'%{phone}%\')'

        self.execute_request(sql_request)

    def get_all(self):
        sql_request = f'SELECT * FROM {self.table_name}'

        self.execute_request(sql_request)

    def get_by_phone(self, phone):
        phone = self.morph_phone(phone)
        sql_request = f'SELECT * FROM {self.table_name} WHERE phone LIKE (\'%{phone}%\')'

        self.execute_request(sql_request)

    def execute_request(self, sql_request):
        with closing(
                psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_request)
                for row in cursor:
                    print(row)

    def morph_phone(self, phone):
        return phone[:-11:-1][::-1]
