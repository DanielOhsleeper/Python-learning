class usdConverter:
    def __init__(
            self,
            add_exchange: list,
            get_exchange: 0,
            update_exchange: list
    ):
        self.add_exchange = []
        self.get_exchange = get_exchange
        self.update_exchange = []

    def addExNis(self, currency: str):
        if currency == "nis":
            nis_rate = "1 USD = 3.16 NIS"
        self.add_exchange = [nis_rate]

    def addExYen(self, currency: str):
        if currency == "yen":
            yen_rate = "1 USD = 113.73 Japanese yen"
        self.add_exchange.append(yen_rate)

    def addExEuro(self, currency: str):
        if currency == "euro":
            euro_rate = "1 USD = 0.89 Euro"
        self.add_exchange.append(euro_rate)

    def getEx(self, from_currency: str, to_currency: str, amount: float):
        if from_currency == "usd" and to_currency == "yen":
            self.get_exchange = f"{amount} {from_currency}={amount * 113.73} Japanese yen"

        if from_currency == "yen" and to_currency == "usd":
            self.get_exchange = f"{amount} {from_currency}={amount / 113.73} USD"

    def update(self, currency: str):
        if currency == "euro":
            euro_rate = "1 USD = 0.96 Euro"
        self.update_exchange = [euro_rate]

    def __str__(self):
        return f"Exchange Rates:\n{self.add_exchange}\nConverter:\n{self.get_exchange}\nUpdated Exchange:\n{self.update_exchange}"

