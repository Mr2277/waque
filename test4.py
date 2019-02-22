import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
text = open('/home/sun/Documents/test.txt','r').read()
tags = jieba.analyse.extract_tags(text, topK=100, withWeight=False)
text = " ".join(tags)
print(text)
bg_pic = imread('3.png')
wordcloud = WordCloud(font_path='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',mask=bg_pic,background_color='white',scale=1.5).generate(text)
image_colors = ImageColorGenerator(bg_pic)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()