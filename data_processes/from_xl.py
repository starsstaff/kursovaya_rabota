from pprint import pprint

import pandas as pd


def excel_to_dict(file_path: str) -> dict:
    # Читаем Excel файл в DataFrame
    df = pd.read_excel(file_path, header=None)

    # Преобразуем первый столбец в ключи, а второй — в значения
    result_dict = dict(zip(df[0], df[1]))

    return result_dict


data = excel_to_dict(r'C:\Users\py\Kursach\iad_sistem_liza\data\туры.xlsx')

pprint(data)