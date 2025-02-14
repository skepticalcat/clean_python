from session2.structure.wikipedia_scraper import get_full_text_wiki_article, get_url_of_wiki_article_of_the_day
from session2.structure.statistics import get_most_common_words
from session2.structure.utils import get_markdown_from_raw_html, split_text_to_word_list, remove_control_chars

article_of_the_day = get_full_text_wiki_article(get_url_of_wiki_article_of_the_day())
markdown_of_wiki_page = get_markdown_from_raw_html(article_of_the_day)
word_list_of_wiki_page = split_text_to_word_list(markdown_of_wiki_page)
word_list_of_wiki_page = [remove_control_chars(x) for x in word_list_of_wiki_page]

text_statistics = get_most_common_words(word_list_of_wiki_page, 10)
print(f"The 10 most common strings are:")
print(text_statistics)