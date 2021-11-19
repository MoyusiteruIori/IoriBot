from nonebot import on_command, CommandSession
from .hairi import hairi

@on_command('牌理')
async def mahjong(session: CommandSession)->str:
    tehai = session.current_arg_text.strip()
    if not tehai:
        tehai = (await session.aget(prompt='你的手牌是？')).strip()
    while not tehai:
        tehai = (await session.aget(prompt='没牌可不能和喔')).strip()
        
    await session.send(hairi(tehai))