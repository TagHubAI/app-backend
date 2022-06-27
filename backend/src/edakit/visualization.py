from wordcloud import WordCloud
import numpy as np
from typing import List

def get_wordcloud_visualization(texts:List[str]) -> np.array: 
    texts = '. '.join(map(str, texts))
    wordcloud = WordCloud(width=800, height=400).generate(texts)
    img = wordcloud.to_array()
    return img