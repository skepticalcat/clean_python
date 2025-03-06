import requests
import re

from clean_python.session2.structure._solution.configs.config import WIKIPEDIA_URL


def get_url_of_wiki_article_of_the_day() -> str:
    wiki_mainpage_result = requests.get(WIKIPEDIA_URL)
    index_of_article_of_day_title = wiki_mainpage_result.text.find("Ukens artikkel (")
    approximate_excerpt_article_of_day = wiki_mainpage_result.text[index_of_article_of_day_title:index_of_article_of_day_title + 500]

    match = re.search(r'<a href="(/wiki/[^"]+)"', approximate_excerpt_article_of_day)

    if match:
        return "https://no.wikipedia.org" + match.group(1)
    else:
        raise LookupError("No article of the day found.")


def get_full_text_wiki_article(url_to_wiki_article: str) -> str:
    return requests.get(url_to_wiki_article).text