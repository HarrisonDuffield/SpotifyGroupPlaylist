import os
DatabaseURL = os.environ['DATABASE_URL']
ClientID = os.environ['SPOTIFY_CLIENT']
ClientSecret = os.environ['SPOTIFY_SECRET']
RedirectURL = os.environ["SPOTIFY_CALLBACK"]



SECRET_KEY  = os.environ['SECRET_KEY']
## Refresh when pushed to heroku, for env variablesss