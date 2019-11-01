from secrets import *
import tweepy
import forecastio
import time

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

latitude =  40.98
longitude = -73.81

forecast = forecastio.load_forecast(api_key, latitude, longitude)
byDay = forecast.daily()

tweet = (byDay.summary)

api.update_status(tweet, latitude, longitude)

#print(api.me())

#print(api.verify_credentials())

#print(api.rate_limit_status())

my_file = open('primes1.txt', 'r')

file_lines = my_file.readlines()

my_file.close()
i = 1

for line in file_lines:

    api.update_status(line)
    time.sleep(1800)
