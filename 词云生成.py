from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba

# 分词
def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result

with open("ping.txt", encoding='utf-8') as fp:
    text = fp.read()
    # print(text)
    # 将读取的中文文档进行分词
    text = trans_CN(text)
    mask = np.array(image.open("ciyun.png"))
    wordcloud = WordCloud(
        # 添加遮罩层
        mask=mask,
        background_color='white',
        font_path = "msyh.ttc"
    ).generate(text)
    image_produce = wordcloud.to_image()
    wordcloud.to_file('cy.png')
    image_produce.show()