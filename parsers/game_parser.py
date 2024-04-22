# Модуль для парсинга заголовка и описания

from parsers.parser import BaseParser


class GameParser(BaseParser):
    """
    Парсер игры
    """

    def parse(self, url: str, xpath_title: str, xpath_description: str, xpath_img: str, xpath_short_description: str,
              xpath_review: str) -> dict:
        """
        Парсинг заголовка и описания
        :param url:
        :param xpath_title:
        :param xpath_description:
        :param xpath_img:
        :return:
        """
        xpath_title = xpath_title.encode('unicode-escape').decode()
        xpath_description = xpath_description.encode('unicode-escape').decode()
        xpath_img = xpath_img.encode('unicode-escape').decode()
        xpath_short_description = xpath_short_description.encode('unicode-escape').decode()
        xpath_review = xpath_review.encode('unicode-escape').decode()
        html = self.get_html_page(url)
        soup = self.html_to_soup(html)
        dom = self.soup_to_etree(soup)
        return {
            'title': self.text_from_dom_by_xpath(dom, xpath_title).strip().replace('\n', ''),
            'description': self.text_from_dom_by_xpath(dom, xpath_description),
            'img': self.src_from_dom_by_xpath(dom, xpath_img).strip().replace('\n', ''),
            'short_description': self.text_from_dom_by_xpath(dom, xpath_short_description).strip().replace('\n', ''),
            'review': self.texts_from_dom_by_xpath(dom, xpath_review)
        }


if __name__ == '__main__':
    parser = GameParser()
    xpath_title = '//div[@class="game-detail-main-overview"]/h2'
    xpath_description = '//*[@id="viewer-9gfc"]/span/span'
    xpath_short_description = '//div[@class="game-detail-main-quick-verdict-content"]/p'
    xpath_img = '//div[@class="game-detail-main-info"]//img'
    xpath_review = '//div[@class="typography"]//p'
    xpath_endpoints = '//a[@class="game-item-name"]'

    url = 'https://kazinoazov.net/Sizzling-Hot-Deluxe-slot-igrat-besplatno'
    result = parser.parse(url, xpath_title, xpath_description, xpath_img, xpath_short_description, xpath_review)
    print(result)