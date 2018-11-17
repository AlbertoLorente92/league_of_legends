# League of Legends

Playing around with the riot api in python

## Getting Started

For my code to work you need to create a .json file name "configuration". This JSON need to contain the keys:

* server
* summonerName
* apikey

With his correspondent values

An example of this could be:

```
{"summonerName":"Blumberg","apikey":"FULL_API_HERE","server":"euw1"}
```

Then you should be good to go

## I don't have an apikey

First for you to have a key you need to have a league of legends account. If you have it or not you should go here:

[TrustMelink](https://auth.riotgames.com/authorize?redirect_uri=https://developer.riotgames.com/oauth2-callback&client_id=riot-developer-portal&response_type=code&scope=openid+email+summoner)

There you can log in or create your new account. 

The "Region" clause in the web is your server. You will need that for the JSON file too. 

If you don't know your region here is a table with the codes:

https://developer.riotgames.com/regional-endpoints.html
