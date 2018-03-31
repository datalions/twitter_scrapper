from tweepy import Cursor, TweepError
from time import sleep
from datetime import date, datetime
from twitter_connection import get_twitter_client
from set_parameters import take_search_words
import json
from pathlib import Path

api = get_twitter_client()
d = date.today()
home = str(Path.home())
file_folder = home + '/Documents/twitter/data/'


def log_to_file(log_text):
    with open(home + '/Documents/twitter/' + str(d) + '_log.txt', 'a+') as l_file:
        l_file.write(log_text)
        l_file.write('\n')


def save_a_tweet(tweets, word_abb):
    tweets = json.dumps({str(d): tweets})
    filename = file_folder + word_abb + '_' + str(d) + '.json'
    with open(filename, 'a+') as f:
        f.write(tweets + '\n')


for word in take_search_words(home + '/Documents/twitter/topics/'):
    c_api = Cursor(api.search, q=word, count=100).items()

    while True:
        try:
            tweet = c_api.next()
            save_a_tweet(tweet._json, word[:3])
            log_correct_tweet = 'Date: {}, Keyword: {}, 1'.format(
                datetime.now(), word
            )
            log_to_file(log_correct_tweet)
        except TweepError:
            with open(home + '/Documents/twitter/log.txt', 'a+') as log_file:
                log_tweep_error = 'Date: {}, Keyword: {}, TweepError - function will start work after 15 min., 2'.format(
                    datetime.now(), word
                )
                log_to_file(log_tweep_error)
            sleep(60 * 15)
            continue
        except StopIteration:
            log_stop_iteration = 'Date: {}, Keyword: {}, 0'.format(
                datetime.now(), word
            )
            log_to_file(log_stop_iteration)
            break
