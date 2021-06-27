import os
import pygsheets
import google.auth
import requests
import numpy as np
import pandas as pd

class gsheet:
    def __init__(self, service_account_file=None):
        if service_account_file:
            self.gc = pygsheets.authorize(service_account_file=service_account_file)
        else:
            credentials, _ = google.auth.default()
            self.gc = pygsheets.authorize(custom_credentials=credentials)

    def post_to_gsheet(self, gsheet_url, gsheet_tab, df):
        """

        :param gsheet_tab:
        :param df:
        :return:
        """

        sh = self.gc.open_by_url(gsheet_url)
        worksheet = sh.worksheet_by_title(gsheet_tab)
        worksheet.set_dataframe(df.fillna(''), (1, 1), fit=True)

        print('data updated on tab {}'.format(gsheet_tab))
