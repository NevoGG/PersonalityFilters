import enum
import os
import openai

import Form

TOP_P = 1
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0
API_KEY = "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"
EXAMPLE_1 = "hanging out with my friends"
EXAMPLE_2 = "I am at the museum"
EXAMPLE_3 = "I am at a Coldplay concert in London"
EXAMPLE_4 = "Hey everybody, I am at the beach"
DV_ENGINE = "text-davinci-002"
COOL_FILTER = "write an extremely laid back version of: \""
MASCULINE_FILTER = "write a very masculine version of: \""
FEMININE_FILTER = "write a feminine version of: \""
VULGAR_FILTER = "write a more vulgar version of: \""
MAX_LINE_LEN = 60

NONE_NUM = 0
MASCULINE_NUM = 1
FEMININE_NUM = 2
COOL_NUM = 3
VULGAR_NUM = 4


def get_max_tokens(prompt):
    word_list = prompt.split()
    return len(word_list) * 7


def get_prompt(f, prompt):
    if f == MASCULINE_NUM:
        return_val = MASCULINE_FILTER + prompt + "\""
    if f == FEMININE_NUM:
        return_val = FEMININE_FILTER + prompt + "\""
    if f == COOL_NUM:
        return_val = COOL_FILTER + prompt + "\""
    if f == VULGAR_NUM:
        return_val = VULGAR_FILTER + prompt + "\""
    if f == NONE_NUM:
        return_val = prompt
    return return_val


class Filters:
    engine = str

    def __init__(self):
        self.engine = DV_ENGINE

    def apply_filter(self, prompt, filter_num):
        prompt_final = get_prompt(filter_num, prompt)
        print(prompt_final + "\n")
        openai.api_key = API_KEY
        max_tokens = get_max_tokens(prompt)
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt_final,
            temperature=0.4,
            max_tokens=max_tokens,
            top_p=TOP_P,
            frequency_penalty=FREQUENCY_PENALTY,
            presence_penalty=PRESENCE_PENALTY
        )
        response_str = response.get("choices")[0].get("text")[2:]
        # if len(response_str) == 0 or response_str[-1] != '.':
        #     if len(response_str) != 0 and response_str.find(".") != -1:
        #         response_str = response_str[:response_str.find(".")]
        #     else:
        #         response = openai.Completion.create(
        #             engine=self.engine,
        #             prompt=prompt_final + "\n" + response_str,
        #             temperature=0.8,
        #             max_tokens=max_tokens,
        #             top_p=TOP_P,
        #             frequency_penalty=FREQUENCY_PENALTY,
        #             presence_penalty=PRESENCE_PENALTY
        #         )
        #         response_str += response.get("choices")[0].get("text")[2:]
        if len(response_str) > MAX_LINE_LEN:
            for i in range(MAX_LINE_LEN):
                if response_str[MAX_LINE_LEN + i] == ' ':
                    response_str = response_str[:MAX_LINE_LEN + i] + "\n" + response_str[MAX_LINE_LEN + i:]
                    break
        print(response_str)
        return response_str



if __name__ == '__main__':
    form = Form.Form()
    form.init()
    openai.api_key = API_KEY
