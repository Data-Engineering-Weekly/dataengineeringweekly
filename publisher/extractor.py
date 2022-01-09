import json

import requests
from bs4 import BeautifulSoup

from publisher.article import Article, DataEngineeringWeekly, DataEngineeringWeeklyEncoder

url_template = "https://www.dataengineeringweekly.com/p/data-engineering-weekly-{edition}"


class Extractor:
    """
    Extractor gets the data engineering weekly url, and extract Article
    """

    def to_json(self, edition: int, indent: int = 4):
        return json.dumps(self.extract_weekly(edition).repr_json(), cls=DataEngineeringWeeklyEncoder, indent=indent)

    def extract_weekly(self, edition: int) -> DataEngineeringWeekly:
        url = url_template.format(edition=edition)
        return DataEngineeringWeekly(edition=edition, articles=self.extract_article(url))

    def extract_article(self, url: str) -> list[Article]:
        response = requests.get(url)
        html_page = response.content
        soup = BeautifulSoup(html_page, 'html.parser')
        article_list = list[Article]()
        for element in soup.find_all("h4"):
            title_text = self.get_author_title(element.get_text())
            author = title_text[0]
            title = title_text[1]
            if author == 'Event' or title == '' or author == 'Sponsored':
                continue
            summary_element = element.next_element.next_element
            summary = summary_element.getText()
            urls = list[str]()
            next_element = summary_element.next_element
            while next_element is not None and next_element.name != "h4":
                if next_element.name == "a":
                    url = next_element.get("href")
                    urls.append(url)
                next_element = next_element.next_element

            if len(urls) > 3:
                urls = urls[0:1]

            article_list.append(Article(author=author, title=title, summary=summary, urls=urls))

        return article_list

    def get_author_title(self, text: str) -> (str, str):
        if text is None or text == "":
            return "", ""
        value = text.split(":")
        return value[0], "".join(value[1: len(value)]).strip()
