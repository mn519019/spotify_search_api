import requests
import simplejson as json

# https://developer.spotify.com/console/get-search-item/?q=blackpink&type=track&market=kr&limit=&offset=&include_external= 

url = "https://api.spotify.com/v1/search"
token ="BQDqHSHO9XiWhDJo83VIzKbTf6uSyaqTmkS60VsTNzKoe8-lmHPdlqUePPHWLgUIHYj1sxbSvTA1Yk5PQQINsO-1sMDsMXecH_mfg22c66jtBg9vjWp3KILdfIw6iXIF03utb_5xndohlO_-oJecoC9Zaxhjadtv1GfGuTjR5cCEkmwC88fWrTqAyXeXKjQ"
#token = {'authorization' : 'Bearer BQCV1nb26WwP2eb4xLhPuFu5cGhT-K9A18xeG0KR84d3DPcocd8k-mfRQOxcDVZI3N3C47GvVTFSQuLY7RfQWVl1hqW02mceX3H5vSjUbb6WoYlbxXV7X8ymEsgqbz9gBzFSAfQVtL637DODpxKwU0vKHNrsvqVfxtcn5rc142zKX3Gqsiwrea9NeMuyYkI'}
param = {'q' : 'blackpink','type' : 'track', 'market' : 'kr'}


def spotify_song_name(arg1):
    response = requests.get('https://api.spotify.com/v1/search',
        headers={ 'authorization': "Bearer " + token}, 
        params={ 'q': 'blackpink', 'type': 'track', 'market' :'kr' })

    status = response.status_code
    data = response.json()['tracks']['items']
    song =""

    if status == 200:
        print("success")
        count=0
        for items in data:
            count += 1 
            #print(count)
            for name in items['album']['name']:
                song = song +" "+ str(name) 
        return "A list of Black Pink's are "+ "\n" +song
    else:
        print("HTTP Status code 200 is not returned, and got ",status)


print(spotify_song_name(str))
