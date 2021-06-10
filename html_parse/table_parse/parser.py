"""
@Project     : html_parse
@Author      : LvYunZe
"""
from abc import ABCMeta
from html.parser import HTMLParser
import pandas as pd


class HtmlTableParser(HTMLParser, metaclass=ABCMeta):
    """
    html表格解析器,可以解析多个表格
    """

    def __init__(
            self,
            decode_html_entities=False,
            data_separator=' ',
            df_list=''
    ):

        HTMLParser.__init__(self, convert_charrefs=decode_html_entities)

        self.df_list = df_list
        self._data_separator = data_separator

        self._in_td = False
        self._in_th = False
        self._current_table = []
        self._current_row = []
        self._current_cell = []
        self.tables = []

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self._in_td = True
        if tag == 'th':
            self._in_th = True

    def handle_data(self, data):
        if self._in_td or self._in_th:
            self._current_cell.append(data.strip())

    def handle_endtag(self, tag):
        if tag == 'td':
            self._in_td = False
        elif tag == 'th':
            self._in_th = False
        if tag in ['td', 'th']:
            final_cell = self._data_separator.join(self._current_cell).strip()
            self._current_row.append(final_cell)
            self._current_cell = []
        elif tag == 'tr':
            self._current_table.append(self._current_row)
            self._current_row = []
        elif tag == 'table':
            self.tables.append(self._current_table)
            self._current_table = []

    def seach_item(self, item, lower=False, blank=False):
        self.df_list = self.get_df_list()
        for df in self.df_list:
            df['name'] = df['name'].str.lower() if lower else df['name']
            df['name'] = df['name'].str.replace(" ", '')
            df_col_len = df.shape[1]
            df.columns = ["name", *[i for i in range(1, df_col_len)]]
            result = df[df.name.str.contains(item)].values[0].tolist()
            return result

    def get_df_list(self):
        df_list = []
        for table in self.tables:
            df = pd.DataFrame(table)
            # 剔除长度为2的DataFrame
            if len(df) <= 2:
                pass
            else:
                df_col_len = df.shape[1]
                df.columns = ["name", *[i for i in range(1, df_col_len)]]
                df_list.append(df)
        return df_list
