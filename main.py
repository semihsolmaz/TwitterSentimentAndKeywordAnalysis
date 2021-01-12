import pandas as pd
import numpy as np
import analyzeKeywords as an
import matplotlib.pyplot as plt


df = pd.read_csv('test.csv')

tweets = df['content'].tolist()




# words in a list
word_counts['words'] = word_counts.index
word_counts.index = range(1, len(word_counts.index)+1)
word_counts = word_counts[word_counts['words'].isin(['first', 'service', 'bug', 'buggy', 'freeze', 'slow', 'crash'])]

print(word_counts)