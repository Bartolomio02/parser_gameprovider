#  Модуль для экспорта данных в формат XLSX

import os
import openpyxl


def export_to_xlsx(data: list, path_to_xlsx: str) -> bool:
    """
    Экспорт данных в файл XLSX
    :param data:
    :param path_to_xlsx:
    :return:
    """
    # data = [
    #     ['name', 'age'],
    #     ['John', 25],
    #     ['Alice', 23],
    # ]
    if not os.path.exists(path_to_xlsx):
        wb = openpyxl.Workbook()
        wb.save(path_to_xlsx)
    wb = openpyxl.load_workbook(path_to_xlsx)
    ws = wb.active
    for row in data:
        ws.append(row)
    wb.save(path_to_xlsx)
    return True


if __name__ == '__main__':
    data = [
        ['name', 'age'],
        ['John', 25],
        ['Alice', 23],
    ]
    path_to_xlsx = 'test.xlsx'
    export_to_xlsx(data, path_to_xlsx)