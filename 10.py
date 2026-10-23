class BankError(Exception):
    pass

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountBlockedError(BankError):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма должна быть больше или равнв 0")

    if amount > balance:
        raise InsufficientFundsError("Недостаточно денег")

    return balance - amount