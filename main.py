from fastapi import FastAPI

from config import fastapi_description, fastapi_version, fastapi_debug, fastapi_title, gp_id
from models import GameProviderParser, GameProviderParserResponse
from parsers.game_parser import GameParser
from parsers.endpoints_parser import EndpointsParser
from export.xlsx import export_to_xlsx
from utils.utils import init_logger
from datetime import datetime

app = FastAPI(title=fastapi_title, description=fastapi_description, version=fastapi_version, debug=fastapi_debug)
app.port = 8001
endpoints_parser = EndpointsParser()
game_parser = GameParser()
logger = init_logger()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/parse_azovkazino", response_model=GameProviderParserResponse)
async def parse_azovkazino(xpath_for_title: str = '//div[@class="game-detail-main-overview"]/h2',
                           xpath_for_description: str = '//*[@id="viewer-9gfc"]/span/span',
                           xpath_for_short_description: str = '//div[@class="game-detail-main-quick-verdict-content"]/p',
                           xpath_for_img: str = '//div[@class="game-detail-main-info"]//img',
                           xpath_for_review: str = '//div[@class="typography"]//p',
                           xpath_for_endpoints: str = '//a[@class="game-item-name"]'):
    """
    Парсер для сайта azovkazino

    :param url:
    :param xpath_for_title:
    :param xpath_for_description:
    :param xpath_for_short_description:
    :param xpath_for_img:
    :param xpath_for_review:
    :param xpath_for_endpoints:
    :return:
    """
    data = [['title', "game providers", 'short description', 'description', 'tags', 'img', 'review']]
    # получаем эдпоинты всех провайдеров
    for gp in gp_id:
        logger.info(f'Parsing {gp}')
        result = endpoints_parser.parse(gp_id[gp], xpath_for_endpoints)
        # парсим каждый эдпоинт
        for url in result['endpoints']:
            logger.info(f'Parsing {url}')
            result = game_parser.parse(url=url, xpath_title=xpath_for_title, xpath_description=xpath_for_description,
                                        xpath_img=xpath_for_img, xpath_review=xpath_for_review, xpath_short_description=xpath_for_short_description)
            data.append([result['title'], gp, result['short_description'], result['description'], '', result['img'], result['review']])
    # экспортируем в xlsx
    export_to_xlsx(data, f'azovkazino_{datetime.now().strftime("%H_%M_%S")}.xlsx')

    return {"code": 200}







