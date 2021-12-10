from nonebot import on_command, CommandSession
from .list import tango, rd_choose
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
        
@on_command('单选单词', aliases=('!tango'))
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