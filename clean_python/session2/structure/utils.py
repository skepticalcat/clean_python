import re

import html2text


def get_markdown_from_raw_html(raw_html: str) -> str:
    h = html2text.HTML2Text()
    h.ignore_links = True

    return h.handle(raw_html)

def split_text_to_word_list(text: str) -> list:
    return text.split(" ")

def remove_control_chars(word: str) -> str:
    return re.sub(r'[\x00-\x1F]+', '', word)