import requests
import simplejson as json

# https://developer.spotify.com/console/get-search-item/?q=blackpink&type=track&market=kr&limit=&offset=&include_external= 

url = "https://api.spotify.com/v1/search"
token ="BQDN7Ef3euMC60Quf5t5BtVxmSL1dI2gjiSKtC_528o-GVyvTnWIOq-RFpd5LLkYzxbCaJPICv4oTBUidUYFpaWpQXwXZ0bGTDIrcrmBR8ORoAxmEtoWilg1ZRkCURevMXWSIbUAr9UH1nRbdNYT5LUKMBLjhLicpsDO8Q8GAE7wpsKtSNipexdu7Fh7564"

def spotify_song_name(arg1):
    response = requests.get('https://api.spotify.com/v1/search',
        headers={ 'authorization': "Bearer " + token}, 
        params={ 'q': 'blackpink', 'type': 'track', 'market' :'kr' })

    status = response.status_code
    data = response.json()['tracks']['items']
    song =""

    if status == 200:
        print("HTTP Request is successful")
        print("The singer is "+data[0]['artists'][0]['name'])
        count=0
        for items in data:
            count += 1 
            for name in items['album']['name']:
                print(str(count)+" song is "+items['album']['name'], end="\n")
                break
    else:
        print("HTTP Status code 200 is not returned, and got ",status)


print(spotify_song_name(str))
#### Expected Output #####
# HTTP Request is successful
# The singer is BLACKPINK
# 1 song is BORN PINK
# 2 song is Pink Venom
# 3 song is SQUARE UP
# 4 song is As If It's Your Last
# .....
# 17 song is BORN PINK
# 18 song is BORN PINK
# 19 song is BORN PINK
# 20 song is BORN PINK
# True
