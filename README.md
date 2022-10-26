# spotify_search_api
We will find  a full list of songs using spotify's API 


## spotify-api-json-parse
Json file parsing using Spotify's APIs result

- A python script to parse JSON data using one of the Spotify's APIs (search api in this case)

## Requirement
- python 3 
- Your own api toekn from Spotify's website
- Understanding the queried JSON structure Main Json Obj vs Array of objects (dictionary)

## Approach 
- When you GET data by sending a HTTP request (request moduel) from python, the data can be cut off on your terminal. I normaly use this site if the api link is provided [JSON Formatter](https://jsonformatter.org/json-pretty-print).
- Otherwise, store your targeted data in the textbox when JSON file is very lengthy

## Reference: 
- https://developer.spotify.com/console/get-search-item/?q=blackpink&type=artist&market=KR&limit=&offset=&include_external=
