import gensim.downloader as api
import pandas as pd
from IPython.core.display import HTML
#info = api.info()  # show info about available models/datasets
#print(info)
data = pd.read_csv('synonyms.csv', sep=",",header=0)