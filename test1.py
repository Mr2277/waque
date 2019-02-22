import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

if __name__ == "__main__":

    mpl.rcParams['font.sans-serif'] = ['FangSong']
    #mpl.rcParams['axes.unicode_minus'] = False
    content = open("/home/sun/Documents/test.txt","rb").read()
    # tags extraction based on TF-IDF algorithm
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
    text =" ".join(tags)
    print(text)
    # read the mask

    d = path.dirname(__file__)
    print(d)

    #trump_coloring = imread(path.join(d, "Trump.jpg"))

    wc = WordCloud(font_path='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',background_color="white", max_words=300, max_font_size=40, random_state=42)

    # generate word cloud
    wc.generate(text)
    '''
    # generate color from image
    image_colors = ImageColorGenerator(trump_coloring)
    
    plt.imshow(wc)
    plt.axis("off")
    #plt.show()
    plt.savefig("test1")
    '''
