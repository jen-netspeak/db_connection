import pandas as pd
import pygsheets
import pymysql.cursors


class MySQLConnection:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def run_query(self, query, gsheet=None, sheet_name=None, gcp_service_json=None):
        connection = pymysql.connect(user=self.user,
                                     password=self.password,
                                     host=self.host,
                                     db=self.database,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        result = pd.read_sql(query, connection)

        if gsheet:
            gc = pygsheets.authorize(service_account_file=gcp_service_json)
            sh = gc.open_by_url(gsheet)
            worksheet = sh.worksheet_by_title(sheet_name)
            worksheet.set_dataframe(result.fillna(''), (1, 1), fit=True)
            print('data posted on gsheet')

        return result


