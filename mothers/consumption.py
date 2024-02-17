from schemas.bill import Consumption


class ConsumptionMother:
    @staticmethod
    def get_daily_consumptions() -> list[Consumption]:
        return [
            Consumption(
                consumption=0.035,
            ),
            Consumption(
                consumption=0.520,
            ),
            Consumption(consumption=0.151),
            Consumption(consumption=0.132),
            Consumption(consumption=0.588),
            Consumption(consumption=0.069),
            Consumption(consumption=0.354),
            Consumption(consumption=0.052),
            Consumption(consumption=0.13),
            Consumption(consumption=0.204),
            Consumption(consumption=0.489),
            Consumption(consumption=0.312),
            Consumption(consumption=0.562),
            Consumption(consumption=0.27),
            Consumption(consumption=0.334),
            Consumption(consumption=0.32),
            Consumption(consumption=0.482),
            Consumption(consumption=0.521),
            Consumption(consumption=0.336),
            Consumption(consumption=0.062),
            Consumption(consumption=0.194),
            Consumption(consumption=0.512),
            Consumption(consumption=0.538),
            Consumption(consumption=0.568),
        ]

    @staticmethod
    def get_weekly_consumptions() -> list[Consumption]:
        return ConsumptionMother.get_daily_consumptions() * 7

    @staticmethod
    def get_monthly_consumptions() -> list[Consumption]:
        return ConsumptionMother.get_weekly_consumptions() * 4
