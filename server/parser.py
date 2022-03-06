import json

from bs4 import BeautifulSoup
import requests


def parser(search_word):
    answer = {"search": search_word}
    link = "https://aliexpress.ru/wholesale?catId=&SearchText=" + search_word
    soup = BeautifulSoup(requests.get(link).text, 'html.parser')

    search_error = soup.find_all("div", {"class": "SearchWrap_SearchError__error__oy8dw"})
    if search_error:
        answer['error'] = "search error"
        return json.dumps(answer, ensure_ascii=False)

    results = soup.find_all("div", {"class": "product-snippet_ProductSnippet__content__mdters"}, limit=10)
    if not results:
        answer['error'] = "connection error"
        return json.dumps(answer, ensure_ascii=False)

    answer['result'] = []
    for result in results:

        has_discount = result.find_all("div", {"class": "snow-price_SnowPrice__discountPercent__18s9w6"})
        if has_discount:
            discount_percent = has_discount[0].get_text()
        else:
            discount_percent = "-0%"

        answer['result'].append(
            {
                "url": "https://aliexpress.ru/" + result.find("a")['href'],

                "price": result.find_all(
                    "div",
                    {"class": "snow-price_SnowPrice__mainM__18s9w6"}
                )[0].get_text().replace(' ', ' '),

                "discount_percent": discount_percent,

                "description": result.find_all(
                    "div",
                    {"class": "product-snippet_ProductSnippet__name__mdters"}
                )[0].get_text(),
            }
        )

    return json.dumps(answer, ensure_ascii=False)
