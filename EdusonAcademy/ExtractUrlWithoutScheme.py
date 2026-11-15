# Создайте функцию extract_url_without_scheme(web_url), которая принимает на вход строку web_url с URL-адресом.
# Используя регулярное выражение r, выполните поиск схемы доступа в URL-адресе.
# Удалите схему доступа из URL-адреса с помощью регулярного выражения trim.
# Верните URL-адрес без указания схемы доступа.

import re
def extract_url_without_scheme(web_url):
    return re.sub(r'^\w+://', '', web_url)