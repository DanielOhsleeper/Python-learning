from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class BankAccount:
    def __init__(self, bank_account: int, name: str):
        self._bank_account = bank_account
        self._name = name
        self._balance = 0
        self._list_of_transactions = []

        self._bank_lock = Lock()
        self._transactions_lock =Lock()



    def deposit(self, amount):
        with self._bank_lock:
            self._balance += amount
        with self._transactions_lock:
            self._list_of_transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        with self._bank_lock:
            self._balance -= amount
        with self._transactions_lock:
            self._list_of_transactions.append(f"Withdraw: {amount}")

    def get_balance(self):
        with self._bank_lock:
            return self._balance


if __name__ == '__main__':
    account = BankAccount(123456, "Israel Israeli")


    def multiple_transactions_deposit(account):
        for i in range(100, 2000000, 10):
            account.deposit(i)


    def multiple_transactions_withdraw(account):
        for i in range(100, 2000000, 10):
            account.withdraw(i)


    with ThreadPoolExecutor(4) as executor:
        executor.submit(multiple_transactions_deposit, account)
        executor.submit(multiple_transactions_withdraw, account)

    assert account._balance == 0, \
        f"Expected balance: 0, received: {account._balance}"
    assert len(account._list_of_transactions) == 399980, \
        f"Expected transactions: 399980, received: {len(account._list_of_transactions)}"


