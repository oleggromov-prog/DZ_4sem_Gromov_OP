def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден")
        return None
    except PermissionError:
        print("Нет прав для для чтения файла")
        return None
    except UnicodeDecodeError:
        print("Невозможно прочитать файл")
        return None
    except IsADirectoryError:
        print("Указанный путь ведет не к файлу, а к папке")
        return None
    except OSError:
        print("Системная оибка")