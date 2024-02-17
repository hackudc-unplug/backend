from transformers import AutoModelForCausalLM, AutoTokenizer


class TipLLMMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(TipLLMMeta, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]


class TipLLM(metaclass=TipLLMMeta):
    tokenizer: AutoTokenizer
    model: AutoModelForCausalLM

    def __init__(self, model_name='stabilityai/stablelm-zephyr-3b'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, trust_remote_code=True, device_map="auto"
        )
        self.top_n = 3

    def get_tip_for_day(
        self, consumptions: list[float], prices: list[float]
    ) -> str:
        indexed_prices = [(i, price) for i, price in enumerate(prices)]
        indexed_consumptions = [
            (i, consumption) for i, consumption in enumerate(consumptions)
        ]

        sorted_prices = sorted(indexed_prices, key=lambda x: x[1], reverse=True)
        sorted_consumptions = sorted(
            indexed_consumptions, key=lambda x: x[1], reverse=True
        )

        most_expensive_hours = [
            index for index, _ in sorted_prices[: self.top_n]
        ]
        least_expensive_hours = [
            index for index, _ in sorted_prices[-self.top_n :]
        ]

        most_consumed_hours = [
            index for index, _ in sorted_consumptions[: self.top_n]
        ]
        least_consumed_hours = [
            index for index, _ in sorted_consumptions[-self.top_n :]
        ]

        prompt = (
            f"Given this data regarding consumption and electricity price for a user, write him some tips to "
            f"improve its cost by suggesting to move high consumption from expensive hours to cheaper hours: "
            f"Three most expensive hours: {most_expensive_hours} Three least expensive hours: "
            f"{least_expensive_hours} Three most consumed hours: {most_consumed_hours} Three least consumed "
            f"hours: {least_consumed_hours}"
        )

        inputs = self.tokenizer.apply_chat_template(  # type: ignore
            [{'role': 'user', 'content': prompt}],
            add_generation_prompt=True,
            return_tensors='pt',
        )

        tokens = self.model.generate(  # type: ignore
            inputs.to(self.model.device),  # type: ignore
            max_new_tokens=1024,
            temperature=0.6,
            do_sample=True,
        )

        return self.tokenizer.decode(tokens[0], skip_special_tokens=False)  # type: ignore
