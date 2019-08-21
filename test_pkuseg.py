import pkuseg

seg = pkuseg.pkuseg(model_name='medicine', postag=True)

text = '我爱北京天安门！'

text = seg.cut(text)
print(text)
