import pytest

from clean_python.session2.structure._solution.src.utils.utils import get_markdown_from_raw_html, split_text_to_word_list, \
    remove_control_chars


def test_get_markdown_from_raw_html():
    raw_html = "<p>Hello <b>World</b></p>"
    markdown = get_markdown_from_raw_html(raw_html)
    assert markdown.strip() == "Hello **World**"

def test_split_text_to_word_list():
    text = "Hello World!"
    words = split_text_to_word_list(text)
    assert words == ["Hello", "World!"]

def test_remove_control_chars():
    word = "Hello\x00World"
    cleaned_word = remove_control_chars(word)
    assert cleaned_word == "HelloWorld"

if __name__ == "__main__":
    pytest.main()