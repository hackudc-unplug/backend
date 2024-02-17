class ConsumptionMother:
    @staticmethod
    def get_daily_consumptions() -> list[float]:
        return [
            0.035,
            0.520,
            0.151,
            0.132,
            0.588,
            0.069,
            0.354,
            0.052,
            0.13,
            0.204,
            0.489,
            0.312,
            0.562,
            0.27,
            0.334,
            0.32,
            0.482,
            0.521,
            0.336,
            0.062,
            0.194,
            0.512,
            0.538,
            0.568,
        ]

    @staticmethod
    def get_weekly_consumptions() -> list[float]:
        return ConsumptionMother.get_daily_consumptions() * 7

    @staticmethod
    def get_monthly_consumptions() -> list[float]:
        return ConsumptionMother.get_weekly_consumptions() * 4
