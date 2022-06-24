"""


Использованы библиотеки:
selenium

Последние изменение: 12.06.2022

"""

import os
from concurrent.futures import ThreadPoolExecutor, wait

import sites

if __name__ == "__main__":

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

    print("Старт......")
    futures = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for cl_site_with_posters in sites.cl_sites_with_posters:
            futures.append(executor.submit(one_site_parse, cl_site_with_posters))
    wait(futures)
    print("Стоп")
