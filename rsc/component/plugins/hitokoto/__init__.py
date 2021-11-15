from nonebot import on_command, CommandSession
from .quotes import otto
from random import choice

@on_command('hitokoto', aliases=('一言'))
async def whos(session : CommandSession):
    unnecessary = session.current_arg_text.strip()
    if not unnecessary:
        sentence = choice(otto)
        await session.send(sentence)
    
