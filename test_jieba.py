import jieba


def test_seg():
    text = '我在北京清华大学上学。'
    """ 精确模式 """
    seg1 = jieba.cut(text)
    print(list(seg1))
    """ 全模式 """
    seg2 = jieba.cut(text, cut_all=True)
    print(list(seg2))
    """ 搜索引擎模式 """
    seg3 = jieba.cut_for_search(text)
    print(list(seg3))


test_seg()
