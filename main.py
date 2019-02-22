import os
import os.path
import codecs

from numpy import unicode

filePaths=[]
fileContents=[]
''''
for root,dirs,files in os.walk('/home/sun/Documents'):
    for name in files:
        filePath=os.path.join(root,name)
        filePaths.append(filePath)
        f=codecs.open(filePath,'r','utf-8')
        fileContent=f.read()
        f.close()
        fileContents.append(fileContent)

import pandas
corpos=pandas.DataFrame({
    'filePath':filePaths,
    'fileContent':fileContents
})
print(corpos)
'''
import jieba
import jieba.analyse
words=jieba.cut("招商银行是商业银行")
print("/".join(words))
tags = jieba.analyse.extract_tags(words, topK=100, withWeight=False)
text=" ".join(tags)
#text=unicode(text)
print(text)