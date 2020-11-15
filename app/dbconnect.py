import psycopg2
import settings
from contextlib import closing


class DbConnection:
    ''' Составление запросов к БД '''

    def __init__(self):
        self.host = settings.host
        self.user = settings.user
        self.password = settings.password
        self.dbname = settings.dbname
        self.table_name = settings.table_name

    def destroy_man(self, phone):
        morph_phone = self.morph_phone(phone)
        if len(phone) < 10:
            return 'Телефон меньше 11 цифр'
        sql_request = f'DELETE FROM {self.table_name} WHERE phone LIKE (\'%{morph_phone}%\')'
        with closing(
                psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)) as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(sql_request)
                except Exception:
                    return 'Ошибка запроса'
                conn.commit()
        return f'Клиент с телефоном {phone} удалён'

    def get_all(self):
        sql_request = f'SELECT * FROM {self.table_name}'

        answer = self.execute_request(sql_request)
        return answer

    def get_by_phone(self, phone):
        phone = self.morph_phone(phone)
        sql_request = f'SELECT * FROM {self.table_name} WHERE phone LIKE (\'%{phone}%\')'

        answer = self.execute_request(sql_request)
        return next(iter(answer), [])

    def execute_request(self, sql_request):
        with closing(
                psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)) as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(sql_request)
                except Exception:
                    return 'Ошибка запроса'
                table = cursor.fetchall()
                answer = []
                for row in table:
                    answer.append(row)
        return answer

    def morph_phone(self, phone):
        return phone[:-11:-1][::-1]
