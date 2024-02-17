from transformers import AutoModelForCausalLM, AutoTokenizer

class TipLLM:
    def __init__(self, model_name='stabilityai/stablelm-zephyr-3b'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            device_map="auto"
        )
        self.top_n = 3

    def get_tip_for_day(self, prices, consumptions):
        indexed_prices = [(i, price) for i, price in enumerate(prices)]
        indexed_consumptions = [(i, consumption) for i, consumption in enumerate(consumptions)]

        sorted_prices = sorted(indexed_prices, key=lambda x: x[1], reverse=True)
        sorted_consumptions = sorted(indexed_consumptions, key=lambda x: x[1], reverse=True)

        most_expensive_hours = [index for index, _ in sorted_prices[:self.top_n]]
        least_expensive_hours = [index for index, _ in sorted_prices[-self.top_n:]]

        most_consumed_hours = [index for index, _ in sorted_consumptions[:self.top_n]]
        least_consumed_hours = [index for index, _ in sorted_consumptions[-self.top_n:]]

        prompt = f"Given this data regarding consumption and electricity price for a user, write him some tips to improve its cost by suggesting to move high consumption from expensive hours to cheaper hours: Three most expensive hours: {most_expensive_hours} Three least expensive hours: {least_expensive_hours} Three most consumed hours: {most_consumed_hours} Three least consumed hours: {least_consumed_hours}"

        inputs = self.tokenizer.apply_chat_template(
            [{'role': 'user', 'content': prompt}],
            add_generation_prompt=True,
            return_tensors='pt'
        )

        tokens = self.model.generate(
            inputs.to(self.model.device),
            max_new_tokens=1024,
            temperature=0.8,
            do_sample=True
        )

        return self.tokenizer.decode(tokens[0], skip_special_tokens=False)


# optimizer = ElectricityCostOptimizer()
# prices = [
#     0.12783, 0.06897, 0.08498, 0.07252, 0.06441, 0.07238, 0.08192, 0.10457,
#     0.08537, 0.11922, 0.06651, 0.11486, 0.08975, 0.10135, 0.12022, 0.11896,
#     0.05318, 0.1296, 0.05933, 0.10104, 0.10676, 0.09229, 0.05173, 0.0578
# ]
# consumptions = [
#     0.035, 0.52, 0.151, 0.132, 0.588, 0.069, 0.354, 0.052, 0.13, 0.204, 0.489,
#     0.312, 0.562, 0.27, 0.334, 0.32, 0.482, 0.521, 0.336, 0.062, 0.194, 0.512,
#     0.538, 0.568
# ]
# answers = optimizer.get_model_answers(prices, consumptions)
# print(answers)
