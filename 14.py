class log_operation:
    def __init__(self, file, operation):
        self.file = file
        self.operation = operation

    def __enter__(self):
        with open(self.file, "a", encoding="utf-8") as file:
            file.write(f"START: {self.operation}\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            i = "ERROR"
        else:
            i = "END"
        with open(self.file, "a", encoding="utf-8") as file:
            file.write(f"{i}: {self.operation}\n")
        return False

with log_operation("operation.log", "Data processing"):
    print("Проверка")

with log_operation("operation.log", "Data processing"):
    raise ValueError()