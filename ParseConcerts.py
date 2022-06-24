"""

Парсер получает информацию о выступлениях с нескольких сайтов
(типа jazzesse.ru/#afisha) и агрегирует в таблицу (data,time,title,desc,price).
Программа разработана с возможностью быстрого добавлению новых сайтов.

Последние изменение: 24.06.2022

"""

import os
from concurrent.futures import ThreadPoolExecutor, wait

import sites

if __name__ == "__main__":

    # В каталог Out складываем результаты для каждого сайта в отдельный файл
    # Создаем Out, если уже есть - очищаем
    if os.path.exists("Out"):
        for the_file in os.listdir('Out'):
            file_path = os.path.join('Out', the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
    else:
        os.mkdir("Out")

    def one_site_parse(cs):
        s = cs()
        s.parse()
        s.save()

    # парсим все сайты в многопотоковом режиме 
    # перебираем все классы из cl_site_with_posters
    print("Старт......")
    futures = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for cl_site_with_posters in sites.cl_sites_with_posters:
            futures.append(executor.submit(one_site_parse, cl_site_with_posters))
    wait(futures)
    print("Стоп")
