import random

tango = {
    'define' : '定义，解释',
    'question' : '怀疑，表示疑问',
    'origin' : '源头，起源',
    'hypothesis' : '假设，假说',
    'refute' : '驳斥',
    'specialize' : '专门研究，专攻',
    'fundamental' : '基础的',
    'evolution' : '进化',
    'microbiology' : '微生物学',
    'zoology' : '动物学',
    'psychology' : '心理学',
    'sociology' : '社会学',
    'anthropology' : '人类学',
    'physical science' : '自然科学',
    
    'accuracy' : '准确，精确',
    'attribute' : '属性，特性',
    'prevailing' : '普遍的，盛行的',
    'technical' : '专业的，专科的',
    'undermine' : '逐渐削弱',
    'suspicion' : '怀疑',
    'explosive' : '炸药，爆炸物',
    'ascertain' : '查明，弄清',
    'consequence' : '结果，后果',
    'proposition' : '提议，建议',
    'devise' : '构想，设计',
    'formulate' : '构想出（计划或提案）',
    'deduction' : '推演，演绎',
    'distinction' : '区别',
    'productive' : '生产力高的',
    'application' : '应用',
    'precept' : '准则，规范',
    'accumulate' : '积累',
    'inquire' : '查询，调查',
    'motion' : '运动，移动',
    'composition' : '成分，构成',
    'disciple' : '信徒，追随者',
    'astronomy' : '天文学',
    'infinitely' : '无限地',
    'geology' : '地质学',
    'particle' : '例子；微粒',
    'immense' : '极大的，巨大的',
    'modus vivendi' : '妥协',
    'celestial body' : '天体',
    'of little/no avail' : '没用',
    'be apt to' : '倾向于',
    'for the sake of' : '为了',
    'in regard to' : '关于，至于',
    'with referrence to' : '遵照'
    
}

def rd_choose(n:int=4) -> list[tuple]:
    answer_ls = random.sample(tango.items(), n)
    return answer_ls
