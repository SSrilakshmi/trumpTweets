import csv
import nltk
nltk.download('punkt')

#top words, given time period

#make list of words
#read in from csv file
words =[]
with open('tweets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
    	i = 0
    	for r in row:
    		#print(r)
    		if i == 0:
    			words.extend(nltk.word_tokenize(r))
    #print(f'Processed {line_count} lines.')

words = [word for word in words if len(word) > 1]
words = [word for word in words if not word.isnumeric()]
words = [word.lower() for word in words]
print(words)

topWords = nltk.FreqDist(words)

for word, frequency in topWords.most_common(50):
    print(u'{};{}'.format(word, frequency))



#we have the tweets, what now?
#set up website?
#analyze
	#top words in a given time period?
	#top topics
	#nicknames
	#emotion
	#capitilization
	#tweet popularity
		#popular in which groups