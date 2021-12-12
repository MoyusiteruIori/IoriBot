import random

tango = {
    # Module1
    'define' :            '定义，解释',
    'question' :          '怀疑，表示疑问',
    'origin' :            '源头，起源',
    'hypothesis' :        '假设，假说',
    'refute' :            '驳斥',
    'specialize' :        '专门研究，专攻',
    'fundamental' :       '基础的',
    'evolution' :         '进化',
    'microbiology' :      '微生物学',
    'zoology' :           '动物学',
    'psychology' :        '心理学',
    'sociology' :         '社会学',
    'anthropology' :      '人类学',
    'physical science' :  '自然科学',
    
    'accuracy' :          '准确，精确',
    'attribute' :         '属性，特性',
    'prevailing' :        '普遍的，盛行的',
    'technical' :         '专业的，专科的',
    'undermine' :         '逐渐削弱',
    'suspicion' :         '怀疑',
    'explosive' :         '炸药，爆炸物',
    'ascertain' :         '查明，弄清',
    'consequence' :       '结果，后果',
    'proposition' :       '提议，建议',
    'devise' :            '构想，设计',
    'formulate' :         '构想出（计划或提案）',
    'deduction' :         '推演，演绎',
    'distinction' :       '区别',
    'productive' :        '生产力高的',
    'application' :       '应用',
    'precept' :           '准则，规范',
    'accumulate' :        '积累',
    'inquire' :           '查询，调查',
    'motion' :            '运动，移动',
    'composition' :       '成分，构成',
    'disciple' :          '信徒，追随者',
    'astronomy' :         '天文学',
    'infinitely' :        '无限地',
    'geology' :           '地质学',
    'particle' :          '例子；微粒',
    'immense' :           '极大的，巨大的',
    'modus vivendi' :     '妥协',
    'celestial body' :    '天体',
    'of little/no avail' : '没用',
    'be apt to' :         '倾向于',
    'for the sake of' :   '为了',
    'in regard to' :      '关于，至于',
    'with reference to' : '遵照',
    
    # Module2
    'nuclear' :           '核的，核武器的',
    'circuit' :           '电路',
    'electricity' :       '电',
    'leftover' :          '剩余的',
    
    'silicon' :           '硅',
    'savvy' :             '洞察力，见解',
    'verify' :            '证实',
    'ventilation' :       '通风',
    'spectrum' :          '光谱；范围',
    'infrastructure' :    '基础设施',
    'construct' :         '建造',
    'electronic' :        '电子的',
    'transform' :         '改变，转变',
    'implement' :         '实现，实施，执行',
    'abstract' :          '抽象的',
    'emission' :          '排放',
    'commercial' :        '商业的',
    'rational' :          '理性的',
    'civil engineering' : '土木工程',
    'electrical engineering' : '电气工程',
    'reinforced concrete' :    '钢筋混凝土',
    
    # Module3
    'advocate' :          '拥护者，支持者',
    'entity' :            '实体',
    'generator' :         '生成器；促使...发生的人',
    'geometry' :          '几何',
    'manifestation' :     '显示，表明',
    'discern' :           '察觉出，识别',
    'proponent' :         '倡导者',
    'laureate' :          '荣誉获得者',
    'axiomatize' :        '使公理化',
    'coin' :              '创造',
    'boast' :             '自夸',
    'cryptography' :      '密码学',
    'sequence' :          '序列',
    'unravel' :           '阐释，说明',
    'replication' :       '复制',
    'stumble upon' :      '偶遇，偶然发现',
    'number theory' :     '数论',
    'string theory' :     '弦理论，弦论',
    'knot theory' :       '结理论，纽结理论',
    
    'comparable' :        '可比的，相当的',
    'handmaiden' :        '女佣人，侍女',
    'occasionally' :      '偶然',
    'affluent' :          '富裕的',
    'doctrine' :          '教义，主义，学说',
    'instrinsic' :        '内在的，本质的',
    'insciribe' :         '在...上写；题；刻',
    'ignorant' :          '无知的',
    'academy' :           '研究院',
    'anguish' :           '剧痛，极度痛苦',
    'gist' :              '要点，主旨',
    'complexity' :        '复杂性',
    'advance' :           '（知识）发展，进展',
    'property' :          '性质，特性',
    'baffle' :            '使困惑',
    'crystallize' :       '使成型，具体化',
    'predecessor' :       '前任，前辈',
    'genius' :            '天资，天才',
    'credit' :            '赞扬',
    'indubitable' :       '明确无疑的',
    'formula' :           '公式；方案',
    'calculus' :          '微积分',
    'analytic geometry' : '解析几何',
    'integral calculus' : '积分学',
    'differential calculus' : '微分学',
    'catch a glimpse of' : '瞥见',
    'by a stretch of imagination' : '想入非非',
    'attend to' :         '处理；注意',
    'take shape' :        '成型，形成',
    'in the air' :        '可感觉到；悬而未决的',
    'down to earth' :     '务实的，脚踏实地的',
    'ascribe to' :        '把...归于...',
    
    # Module 4
    'comprehensive' :     '全部的',
    'predict' :           '预言',
    'dash' :              '破折号',
    'Sankrit' :           '梵语',
    'exclusive' :         '专用的，专有的',
    'conduct' :           '传导（热或电）',
    'atomic weight' :     '原子量',
    'melting point' :     '熔点',
    'Celsius' :           '摄氏的',
    'Fahrenheit' :        '华氏的',
    'The periodic table of the elements' : '元素周期表',
    'crystal' :           '结晶，晶体',
    'incorporate' :       '包含',
    'organism' :          '生物；微生物',
    'inanimate' :         '无生命的',
    'spark' :             '火花，火星',
    'abundant' :          '丰富的',
    'potential' :         '潜力，可能性',
    'reactivity' :        '反应性',
    'provocation' :       '挑衅',
    'harness' :           '利用；治理',
    'multitask' :         '使多任务化',
    'restrictive' :       '约束性的',
    'alternative' :       '替代品',
    'bond' :              '建立关系',
    'versatile' :         '用途广泛的',
    'ingredient' :        '原料, 成分, 要素',
    'fabricate' :         '制造，编造',
    'eliminate' :         '排除，清除',
    'inflexible' :        '不可改变的',
    'requisite' :         '必须的，必备的',
    'genetic' :           '遗传的',
    'competition' :       '竞争',
    'mineral' :           '矿物质',
    'hydrogen' :          '氧',
    'helium' :            '氦',
    'inert' :             '惰性的',
    'molecular' :         '分子的',
    'lithium' :           '锂',
    'beryllium' :         '铍',
    'boron' :             '硼',
    'nitrogen' :          '氮',
    'crust' :             '地壳',
    'mantle' :            '地幔',
    'magnesium' :         '镁',
    'calcium' :           '钙',
    'oxygen' :            '氧',
    'neon' :              '氖',
    'argon' :             '氩',
    'fluorine' :          '氟',
    'aluminum' :          '铝',
    'sulfur' :            '硫',
    'chlorine' :          '氯',
    'be adept to' :       '擅长',
    'conform to' :        '遵照，顺应',
    'dwindle' :           '（逐渐）减小，变小',
    'flaw' :              '错误，缺点',
    'promising' :         '前景很好的',
    'adaptable' :         '能适应的',
    'biosphere' :         '生物圈',
    'protein' :           '蛋白质',
    'amino acid' :        '氨基酸',
    'burst into flames' : '突然起火',
    'sturdy and stable' : '结实的，坚固的',
    'cross off' :         '（从名单上）删掉，取消',
    'wind up' :           '完成，停止',
    'in vain' :           '徒劳，无效',
    'shy away' :          '避开，避免接触',
    
    #Module 5
    'theoretical' :       '理论上的',
    'persistent' :        '执着的，坚持不懈的',
    'pursuit' :           '追求',
    'anniversary' :       '周年纪念日',
    'cosmology' :         '宇宙学',
    'stun' :              '使震惊',
    'radiate' :           '辐射',
    'distinguished' :     '卓越的',
    'deteriorate' :       '恶化，变坏',
    'synthesizer' :       '语音合成器',
    'profound' :          '知识渊博的；深邃的；深刻的',
    'humanity' :          '（统称）人；人类',
    'celebrity' :         '名人；名流',
    'thermodynamics' :    '热力学',
    'motor neuron' :      '运动神经元',
    
    'inherently' :        '内在的，固有的，生来就有的',
    'indivisible' :       '不可分的',
    'charge' :            '负荷',
    'irregular' :         '无规律的',
    'collide' :           '碰撞',
    'filament' :          '灯丝',
    'internal' :          '内部的',
    'radioavtive' :       '放射性的，有辐射的',
    'resign' :            '辞职',
    'dispute' :           '争论',
    'enigmatic' :         '神秘的，费解的，令人困惑的',
    'rhyme' :             '押韵',
    'imaginative' :       '想象力丰富的',
    'decay' :             '腐坏',
    'electron' :          '电子',
    'proton' :            '质子',
    'neutron' :           '中子',
    'mass' :              '质量',
    'quark' :             '夸克',
    'compound' :          '化合物',
    'Brownian motion' :   '布朗运动',
    'The Fellows' :       '学院院士',
    
    # Module 6
    'orchestration' :     '管弦乐曲',
    'lateral' :           '侧面的，横向的',
    'lens' :              '镜头',
    
    'graphical' :         '图解的',
    'testify' :           '作证',
    'indigenous' :        '本土的，当地的',
    'hostile' :           '反对的，敌对的',
    'skeleton' :          '（楼房）构架；框架',
    'lintel' :            '（建筑学）过梁',
    'fenestration' :      '窗户设计',
    'beam' :              '梁',
    'counteract' :        '抵消',
    'traperzoidal' :      '梯形的',
    'eulogize' :          '称赞',
    'stylobate' :         '柱座',
    'post' :              '立柱',
    'pitched' :           '倾斜的',
    'literary' :          '文学的；书面的',
    'retain' :            '保留',
    'perpetuate' :        '使不朽；保持',
    'proportion' :        '部分；比例',
    'adaptability' :      '适应性',
    'oblong' :            '长方形',
    'potentiality' :      '潜力，潜能',
    'analogous' :         '类似的',
    'osseous' :           '框架的',
    'topography' :        '地形',
    'tier' :              '排，层',
    'corbel' :            '托臂；枕梁',
    'timber' :            '木材',
    'interior partition': '内部隔断',
    'exemplary' :         '堪称典范的',
    'prevalent' :         '普遍存在的',
    'military' :          '军事的',
    'render' :            '使成为，使变得',  # It contained so many errors as to render it worthless
    'monumental' :        '宏伟的',
    'principal axis' :    '中轴线',
    'structural system' : '结构体系',
    'plan arrangement' :  '平面布局',
    'overhanging eaves' : '飞檐',
    'auxiliary building': '附属建筑',
    'the elements' :      '恶劣天气'
}

def rd_choose(n:int=4) -> list[tuple]:
    answer_ls = random.sample(tango.items(), n)
    return answer_ls
