from nonebot import on_command, CommandSession
from .data_resource import find_murderer

# 小群玩梗自用
@on_command('谁的', only_to_me=False)
async def whos(session : CommandSession):
    unnecessary = session.current_arg_text.strip()
    if not unnecessary:
        murderer = find_murderer()
        await session.send(murderer + '的')
    
