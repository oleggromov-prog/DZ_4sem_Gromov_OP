import re
import json
import logging

logging.basicConfig(level = logging.INFO, format="%(levelname)s: %(message)s")

c_get = 0
c_post = 0
c_errors = 0
urls = []
m_c_url = 0
m_url = ""

logging.info("Программа начинает работу")

try:
    with open("access.log", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            l = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ([A-Z]+) (/[^\s]+) (\d{3})", line)[0]
            if l[1] == "GET":
                c_get += 1
            if l[1] == "POST":
                c_post += 1

            if 400 <= int(l[3]) <= 499:
                c_errors += 1

            urls.append(l[2])
except FileNotFoundError:
    logging.error("Файл не найден")
    raise
except PermissionError:
    logging.error("Нет прав для для чтения файла")
    raise
except UnicodeDecodeError:
    logging.error("Невозможно прочитать файл")
    raise
except IsADirectoryError:
    logging.error("Указанный путь ведет не к файлу, а к папке")
    raise
except OSError:
    logging.error("Системная оибка")
    raise

for url in urls:
    c = urls.count(url)
    if c > m_c_url:
        m_c_url = c
        m_url = url

stats = {"c_get" : c_get, "c_post" : c_post, "c_errors" : c_errors, "frequent_url" : m_url}

with open("18stat.json", "w", encoding="utf-8") as file:
    json.dump(stats, file, indent=4)

logging.info("Программа успешно завершилась")