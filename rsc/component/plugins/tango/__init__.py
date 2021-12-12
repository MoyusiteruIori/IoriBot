from nonebot import on_command, CommandSession
from .list import tango, rd_choose
import asyncio
import random

@on_command('单词', aliases=('word', 'tango', '単語'))
async def write_eng(session:CommandSession):
    answers = rd_choose(4)
    right_eng, right_chn = random.choice(answers)
    answer = (await session.aget(prompt=f'哼~哼~哼~\n「{right_chn}」\n它的英文是什么呢~')).strip()
    if(answer == right_eng):
        await session.send('答对啦')
    else:
        await session.send(f'笨蛋，答案是{right_eng}')
        
@on_command('汉译选英', )
async def choose_eng(session:CommandSession):
    answers = rd_choose(4)
    ans_dict = dict(zip([word[0] for word in answers], ['A','B','C','D']))
    right_ans = random.choice(answers)
    answer = (await session.aget(
        prompt=f'哼~哼~哼~\n下面哪一项的意思是「{right_ans[1]}」呢？\n'
        + f'A {answers[0][0]}\n'
        + f'B {answers[1][0]}\n'
        + f'C {answers[2][0]}\n'
        + f'D {answers[3][0]}\n'
        ))
    if(answer[0] == ans_dict[right_ans[0]]):
        await session.send('答对啦')
    else:
        await session.send(f'笨蛋，答案是「{right_ans[0]}」')
        
        
@on_command('单词连发', aliases=('TangoCombo'))
async def tango_combo(session:CommandSession):
    while True:
        answers = rd_choose(4)
        right_eng, right_chn = random.choice(answers)
        answer = (await session.aget(prompt=f'哼~哼~哼~\n「{right_chn}」\n它的英文是什么呢~')).strip()
        if(answer == 'stop'):
            break
        if(answer == right_eng):
            await session.send('答对啦')
        else:
            await session.send(f'笨蛋，答案是{right_eng}')
        await asyncio.sleep(0.5)
    await session.send('结束~~')
    
@on_command('英文选义')
async def choose_chn(session:CommandSession):
    answers = rd_choose(4)
    ans_dict = dict(zip([word[1] for word in answers], ['A','B','C','D']))
    right_ans = random.choice(answers)
    answer = (await session.aget(
        prompt=f'哼~哼~哼~\n「{right_ans[0]}」是什么意思呢？\n'
        + f'A {answers[0][1]}\n'
        + f'B {answers[1][1]}\n'
        + f'C {answers[2][1]}\n'
        + f'D {answers[3][1]}\n'
        ))
    if(answer[0] == ans_dict[right_ans[1]]):
        await session.send('答对啦')
    else:
        await session.send(f'笨蛋，答案是「{right_ans[1]}」')
        

@on_command('英文选义combo')
async def choos_chn_combo(session:CommandSession):
    while True:
        answers = rd_choose(4)
        ans_dict = dict(zip([word[1] for word in answers], ['A','B','C','D']))
        right_ans = random.choice(answers)
        answer = (await session.aget(
            prompt=f'哼~哼~哼~\n「{right_ans[0]}」是什么意思呢？\n'
            + f'A {answers[0][1]}\n'
            + f'B {answers[1][1]}\n'
            + f'C {answers[2][1]}\n'
            + f'D {answers[3][1]}\n'
            ))
        if(answer == 'stop'):
            break
        if(answer[0] == ans_dict[right_ans[1]]):
            await session.send('答对啦')
        else:
            await session.send(f'笨蛋，答案是「{right_ans[1]}」')
    await session.send('结束~~~')