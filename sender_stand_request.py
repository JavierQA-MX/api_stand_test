import requests

from api_stand_test import configuration

import data

'''
Esta palabra clave "import"  se assures de import la info del archivo 
configuration.py y el paquete pip downloaded "requests"
Accessing a las constants defined por archives
'''
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
#Cuando se llama esta function makes una solicitude GET al file con el destino y clave
#Cuando se utiliza JSON es para decirle al sistema el tipo de lenguage con el que se esta introduciendo el codigo

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         headers=data.headers,
                         json=body)
response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)

response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())

