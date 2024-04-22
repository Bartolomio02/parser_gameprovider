# Базовый класс для всех парсеров
# Все парсеры должны наследоваться от этого класса

from abc import ABC, abstractmethod
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup
from lxml import etree


class BaseParser(ABC):
    """
    Базовый класс для всех парсеров
    """

    def __init__(self):
        self.url = 'https://kazinoazov.net/frontendService/gamesFilterServiceMore'

    def get_html_page(self, url: str) -> requests.models.Response:
        """
        Получение HTML страницы
        :param url:
        :return:
        """
        HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                    'Accept-Language': 'en-US, en;q=0.5'})
        return requests.get(url, headers=HEADERS)

    def post_html_page(self, url: str, gp_id: str, page: str) -> requests.models.Response:
        """
        Получение HTML страницы
        :param url:
        :param gp_id:
        :param page:
        :return:
        """
        params = {
            'page': page,
            'initialPage': '1',
        }

        data = {
            f'gp_{gp_id}': 'true',
            'paginate_by': '1',
        }

        return requests.post(url, params=params, data=data)

    def html_to_soup(self, html: requests.models.Response) -> BeautifulSoup:
        """
        Преобразование HTML в объект BeautifulSoup
        :param html:
        :return:
        """
        return BeautifulSoup(html.content, 'html.parser')

    def soup_to_etree(self, soup: BeautifulSoup) -> etree:
        """
        Преобразование объекта BeautifulSoup в объект etree
        :param soup:
        :return:
        """

        return etree.HTML(str(soup))

    def text_from_dom_by_xpath(self, dom: Any, xpath: str) -> str:
        """
        Получение текста из объекта dom по XPath
        :param dom:
        :param xpath:
        :return:
        """
        try:
            return dom.xpath(xpath)[0].text
        except:
            return ''

    def texts_from_dom_by_xpath(self, dom: Any, xpath: str) -> str:
        """
        Получение текста из объектов dom по XPath
        :param dom:
        :param xpath:
        :return:
        """
        # try:
        texts = [a.text for a in dom.xpath(xpath)]
        response = ''
        for i in range(len(texts)):
            if texts[i] != None:
                response += texts[i]
        return response


        # except:
        #     return ''

    def href_from_dom_by_xpath(self, dom: Any, xpath: str) -> list:
        """
        Получение ссылок из объекта dom по XPath
        :param dom:
        :param xpath:
        :return:
        """
        try:
            return [a.get('href') for a in dom.xpath(xpath)]
        except:
            return []


    def src_from_dom_by_xpath(self, dom: Any, xpath: str) -> str:
        """
        Получение ссылки из объекта dom по XPath
        :param dom:
        :param xpath:
        :return:
        """
        try:
            return dom.xpath(xpath)[0].get('src')
        except:
            return ''

    @abstractmethod
    def parse(self, *args, **kwargs) -> Any:
        """
        Парсинг страницы
        :param args:
        :param kwargs:
        :return:
        """
        pass
