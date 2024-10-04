
data_list_tabel = {
    'tour_name': {
        'name': 'name',
        'season': ['Лето ', 'Осень', 'Зима', 'Весна', 'Универсальный'],
        'price_col': [
            {
                'price_base': 10000,

                'duration_range': 'от 3 до 21',
                'clients_num_range': {
                    'min': 1,
                    'max': 'int_max'
                },
                'base_duration price': '20 процентов от price_base * seasons * region_ratio',
                'regin': 'str'

            }
        ],
        'regin': 'str'
    }

}

data_list_dataset = {
    'tour_name': 'tour_id',
    'client_id': 'id',
    'season': 'tour[tour_name][season]',
    'price': 'calculate(((price_base + (one_client_price * clients_len)) * season_ratio * region_ratio))'
}

data_list_tabel_2 = {
    'name': str,
    'season': list(str),
    'price': float,
    'region': str,
    'duration_range': int,
    'clients_max': int,


}