class PriceMother:
    @staticmethod
    def get_daily_prices() -> list[float]:
        return [
            0.12783,
            0.06897,
            0.08498,
            0.07252,
            0.06441,
            0.07238,
            0.08192,
            0.10457,
            0.08537,
            0.11922,
            0.06651,
            0.11486,
            0.08975,
            0.10135,
            0.12022,
            0.11896,
            0.05318,
            0.1296,
            0.05933,
            0.10104,
            0.10676,
            0.09229,
            0.05173,
            0.0578,
        ]

    @staticmethod
    def get_weekly_prices() -> list[float]:
        return PriceMother.get_daily_prices() * 7

    @staticmethod
    def get_monthly_prices() -> list[float]:
        return PriceMother.get_weekly_prices() * 4
