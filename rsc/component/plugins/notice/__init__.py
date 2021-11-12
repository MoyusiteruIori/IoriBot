from aiocqhttp.message import MessageSegment
from nonebot import on_notice, CommandSession
import os
from config import IMGAE_LOCAL_MEME
from random import choice


@on_notice()
async def notice(session:CommandSession):
    img = [f for f in os.listdir(IMGAE_LOCAL_MEME) if f.endswith('jpg') or f.endswith('png')]
    selected_img = choice(img)
    seq = MessageSegment.image('file:///{}'.format(IMGAE_LOCAL_MEME + selected_img))
    await session.send(seq)
