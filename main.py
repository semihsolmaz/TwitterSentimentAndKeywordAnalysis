import pandas as pd
import numpy as np
import analyzeKeywords as an
import matplotlib.pyplot as plt


df = pd.read_csv('test.csv')

tweets = df['content'].tolist()

word_count = an.get_most_used_words(tweets)

# words in count
word_counts = pd.DataFrame.from_dict(word_count,orient='index',columns=['counts']).sort_values('counts', ascending=False).head(20)
count_graph = word_counts['counts'].plot.bar(y='counts', rot=90)
plt.show()


# words in a list
word_counts['words'] = word_counts.index
word_counts.index = range(1, len(word_counts.index)+1)
word_counts = word_counts[word_counts['words'].isin(['first', 'service', 'bug', 'buggy', 'freeze', 'slow', 'crash'])]

print(word_counts)