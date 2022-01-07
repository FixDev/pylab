import tweepy
import csv

consumer_key = 'JrdyWogkaURhtmGjYeiUDw0kY'
consumer_secret = 'L9u1y6orT0wvVM3PqoyDf8JOrzgDUM3RFeFT4a5zFDVGOOV5xi'
access_token = '1440539684480847872-0YKSjFgscFZQ8eT7Tayue6h9oLFSaI'
access_secret = '3frdxhrojAuyedg009Yy7sbXo3I0Kc2pO8rn7ZqpyxlGI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
# Open/create a file to append data to
csvFile = open('nama-file.csv', 'w', encoding='utf-8')
# Use csv writer
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search_30_day, query='#PPKM -filter:retweets', label="PPKM").items(100):
    text = tweet.full_text
    user = tweet.user.name
    created = tweet.created_at
    csvWriter.writerow([created, text.encode('utf-8'), user])
csvWriter = csv.writer(csvFile)
csvFile.close()
