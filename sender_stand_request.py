import configuration
import requests
import data

# Функция создания нового заказа

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,
                         json=body,
                         headers=data.headers
                         )
# Функция получения заказа по трекеру

def get_order(parameters):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER,
                        params=parameters
                        )
