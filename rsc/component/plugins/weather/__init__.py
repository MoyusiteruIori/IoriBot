from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg

from .data_source import *

@on_command("weather", aliases=("天气", "天气预报", "查询天气"))
async def weather(session : CommandSession):
    city = session.current_arg_text.strip()
    if not city:
        city = (await session.aget(prompt='你想查询哪个城市的天气呢？')).strip()
        while not city:
            city = (await session.aget(prompt='要查询的城市不能为空哦')).strip()
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)


@on_natural_language(keywords={'天气'})
async def _(session : NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)

    city = None
    for word in words:
        if word.flag == 'ns':
            city = word.word
            break

    return IntentCommand(90.0, 'weather', current_arg=city or '')