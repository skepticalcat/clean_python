from collections import Counter



def get_most_common_words(word_list: list, amount: int):
    return Counter(word_list).most_common(amount)