# Модели для валидации данных FastAPI

from pydantic import BaseModel, Field


class GameProviderParser(BaseModel):
    url: str = Field(description="URL на страницу с названием и описанием игры", example="https://www.example.com",
                     title="URL на страницу")
    xpath_for_title: str = Field(description="XPath на название игры", example="//h1", title="XPath на название игры")
    xpath_for_description: str = Field(description="XPath на описание игры", example="//p",
                                       title="XPath на описание игры")


class GameProviderParserResponse(BaseModel):
    code: int = Field(description="Статус ответа", example=200, title="Статус ответа")
    # data: dict = Field(description="Данные ответа",
    #                    example={"url": "https://www.example.com", "title": "Game name", "description": "Cool game"},
    #                    title="Данные ответа")
ІІ