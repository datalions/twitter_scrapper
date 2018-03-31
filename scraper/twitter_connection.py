import set_parameters
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter connection
    return: API object"""

    parameters = set_parameters.take_auth_data()

    twitter_access_token = parameters['twitter_access_token']
    twitter_secret_token = parameters['twitter_secret_token']
    twitter_api_key = parameters['twitter_api_key']
    twitter_secret_key = parameters['twitter_secret_key']

    auth = OAuthHandler(twitter_api_key, twitter_secret_key)
    auth.set_access_token(twitter_access_token, twitter_secret_token)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client

if __name__ == '__main__':
    a = get_twitter_client()
    print(a)