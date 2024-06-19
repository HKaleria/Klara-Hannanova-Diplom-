# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания нового заказа в системе
# содержат имя, фамилию, адрес заказчика, ближайшую к заказчику станцию метро, телефон заказчика,
# количество дней аренды,дату доставки,комментарий от заказчика, цвет
order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
params_get = {
    "t": ""
}