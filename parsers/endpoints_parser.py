# Модуль для парсинга конечных точек игр

from parsers.parser import BaseParser
from config import gp_id


class EndpointsParser(BaseParser):
    """
    Парсер конечных точек игр
    """

    def parse(self, gp_id: str, xpath_endpoints: str) -> dict:
        """
        Парсинг конечных точек игр
        :param gp_id:
        :param xpath_endpoints:
        :return:
        """
        xpath_endpoints = xpath_endpoints.encode('unicode-escape').decode()
        endpoints_list = []
        page = 1
        while True:
            print(page)
            html = self.post_html_page(self.url, gp_id, str(page))
            soup = self.html_to_soup(html)
            dom = self.soup_to_etree(soup)
            endpoints = self.href_from_dom_by_xpath(dom, xpath_endpoints)
            print(endpoints)
            if len(endpoints) > 0:
                endpoints_list.extend(endpoints)
                page += 1
            else:
                break
        return {
            'endpoints': endpoints_list
        }


if __name__ == '__main__':
    parser = EndpointsParser()
    xpath_endpoints = '//a[@class="game-item-name"]'
    xpath_endpoints = xpath_endpoints.encode('unicode-escape').decode()

    result = parser.parse(gp_id['paragmatic play'], xpath_endpoints)
    for x in result['endpoints']:
        print(x)
    print(len(result['endpoints']))
