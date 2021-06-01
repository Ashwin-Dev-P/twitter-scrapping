import sys,tweepy

def twitter_auth():
    try:
        customer_key = ''
        customer_secret = ''
        access_token = ''
        access_secret = ''
    except KeyError:
        sys.stderr.write("TWITTER_* environment variable not set\n")
        sys.exit(1)
        
    auth = tweepy.OAuthHandler(customer_key, customer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth,wait_on_reate_limit=True)
    return client

if __name__ == '__main__':
            
        
        
        
        
        
        
        
        