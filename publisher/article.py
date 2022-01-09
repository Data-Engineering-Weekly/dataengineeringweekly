from __future__ import annotations

import json
from dataclasses import dataclass, astuple
from json import JSONEncoder


@dataclass
class DataEngineeringWeekly:
    edition: int
    articles: list[Article]

    def __iter__(self):
        return iter(astuple(self))

    def repr_json(self):
        return dict(edition=self.edition, articles=self.articles)


@dataclass
class Article:
    """
        Article is the container for all the data engineering weekly contents.
        1. article publisher
        2. article title
        3. summary
        4. list of url for the articles
        """
    author: str
    title: str
    summary: str
    urls: list[str]

    def __iter__(self):
        return iter(astuple(self))

    def repr_json(self):
        return dict(author=self.author, title=self.title, summary=self.summary, urls=self.urls)


class DataEngineeringWeeklyEncoder(JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'repr_json'):
            return obj.repr_json()
        else:
            return json.JSONEncoder.default(self, obj)
