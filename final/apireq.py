# by jasmine
# april 2017
# final v 0.0.1
# tests for documentation

import sys
import keys
import twython
from twython import Twython, TwythonError

# # from allison's notes
# # these work but I want to search by location

# api_key, api_secret, access_token, token_secret = sys.argv[1:]
twitter = twython.Twython(keys.api_key, keys.api_secret, keys.access_token, keys.token_secret)

# # Example 1
response = twitter.search(q="data journalism", result_type="recent", count=4)
[r['text'] for r in response['statuses']]
print response

# # Example 2
query = "sea rose"

response = twitter.search(q=query, result_type="recent", count=20)
for tweet in response['statuses']:
    print tweet['text']


# # things that don't seem to work?
# # or there are no geocoded tweets

# # (1) something prints but doesn't included statuses
# twitter = Twython(api_key, api_secret, access_token, token_secret)

geocode = '40.72, -73.95, 10mi' # latitude,longitude,distance(mi/km)

try:
    searches = twitter.search(count=100, geocode=geocode)
    print(searches)
except TwythonError as e:
    print(e)


# # (2) nothing prints

# search_results = twitter.search(count=100, geocode=geocode)
#
# try:
#     for tweet in search_results['statuses']:
#         print (tweet['text'])
# except TwythonError as e:
#     print(e)
