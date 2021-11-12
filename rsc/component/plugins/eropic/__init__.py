from aiocqhttp.message import MessageSegment
from nonebot import on_command, CommandSession
from .pic_info import *
from config import IMAGE_LOCAL_BUFF


@on_command('涩图', aliases=('色图', '色色'))
async def eropic(session : CommandSession):
    pic = GetPic()
    await pic.get_pic()
    seq = MessageSegment.image('file:///{}'.format(IMAGE_LOCAL_BUFF))
    await session.send(seq, at_sender=True)
