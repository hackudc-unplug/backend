from schemas.bill import Price


class PriceMother:
    @staticmethod
    def get_daily_prices() -> list[Price]:
        return [
            Price(price=0.12783),
            Price(price=0.06897),
            Price(price=0.08498),
            Price(price=0.07252),
            Price(price=0.06441),
            Price(price=0.07238),
            Price(price=0.08192),
            Price(price=0.10457),
            Price(price=0.08537),
            Price(price=0.11922),
            Price(price=0.06651),
            Price(price=0.11486),
            Price(price=0.08975),
            Price(price=0.10135),
            Price(price=0.12022),
            Price(price=0.11896),
            Price(price=0.05318),
            Price(price=0.1296),
            Price(price=0.05933),
            Price(price=0.10104),
            Price(price=0.10676),
            Price(price=0.09229),
            Price(price=0.05173),
            Price(price=0.0578),
        ]

    @staticmethod
    def get_weekly_prices() -> list[Price]:
        return PriceMother.get_daily_prices() * 7

    @staticmethod
    def get_monthly_prices() -> list[Price]:
        return PriceMother.get_weekly_prices() * 4
