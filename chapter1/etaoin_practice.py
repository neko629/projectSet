"""统计一个句子中出现 etaion 字母的次数, 不区分大小写."""

LETTERS = "etaion"

INPUT_SENTENCE = "Once upon a day, there was a wolf who lived in the forest"

letter_dict = {}

def init_letter_dict():
    """Init LETTER_DICT with empty lists."""
    for s in LETTERS:
        letter_dict[s] = []


def letter_counter(sentence: str):
    """Count the occurrences of letters in LETTERS within the sentence."""
    sentence = sentence.lower()
    for x in sentence:
        if x in LETTERS:
            letter_dict[x].append(x)

    print_result(letter_dict)

def print_result(result_dict):
    """按行打印结果."""
    for letter, _list in result_dict.items():
        print(f"{letter}: {_list}")


if __name__ == "__main__":
    init_letter_dict()
    letter_counter(INPUT_SENTENCE)
