from gensim.models import Word2Vec
import gensim.utils

text = []
for ind in range(48):
    indstr = str(ind)
    filename = "obama_speeches_" + str(indstr.zfill(3)) + ".txt" #위치는 .py파일위치에 두기,  #zfill은 빈자리 0채우는 갯수
    with open(filename) as file:
        line = file.readline()
        while line:
            text.append(gensim.utils.simple_preprocess(line))
            line = file.readline()

ob = Word2Vec(text, size=10, window=5, min_count=1, workers=4) #size 벡터의 차원
ob.train(text, total_examples=len(text), epochs=100) #epochs 반복횟수

print(ob.wv['war'])

ob.wv.most_similar(positive='people')


'''이제 trump 부분코드'''
from gensim.models import Word2Vec
import gensim.utils

text = []
for ind in range(18):
    indstr = str(ind)
    filename = "trump_speeches_" + str(indstr.zfill(3)) + ".txt"
    with open(filename) as file:
        line = file.readline()
        while line:
            text.append(gensim.utils.simple_preprocess(line))
            line = file.readline()

dt = Word2Vec(text, size=10, window=5, min_count=1, workers=4) #오바마와 트럼프 학습 환경 일치시키기
dt.train(text, total_examples=len(text), epochs=100) #오바마와 트럼프 학습 환경 일치시키기

print(dt.wv['war'])

dt.wv.most_similar(positive='people')
