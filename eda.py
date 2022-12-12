
import pandas as pd 
import plotly_express as px
import plotly.graph_objects as go

# first dataset
url1 = 'https://media.githubusercontent.com/media/dataPracticum/codepudding/main/spotify/spotify_dataset.csv'
full = pd.read_csv(url1, on_bad_lines='skip', names=['user_id', 'artist_name', 'track_name', 'playlist_name'])


# artists of the decade
number = [5, 10, 20, 50, 100]
for n in number:
    top_artist = full.artist_name.value_counts().nlargest(n)
    px.bar(top_artist, title='Top ' + str(n) +  ' Most Common Artists of the Decade', height=600).show()


# artist of the decade percentage
number = [5, 10, 20]
for n in number:
    top_artist = full.artist_name.value_counts(normalize=True).nlargest(n) * 100
    px.bar(top_artist, title='Top ' + str(n) +  ' Most Common Artists of the Decade as Percentage', height=600, log_y=True).show()


# playlists of the decade
number = [5, 10, 15, 25]
for n in number:
    top_playlists = full.playlist_name.value_counts().nlargest(n)
    px.bar(top_playlists, title='Top ' + str(n) +  ' Most Common Playlists of the Decade', height=600).show()


# compound of categories and playlist, n iterations
number = [5, 10, 20, 50, 100]
categories = ['artist_name', 'playlist_name']
for n in number:
    for category in categories:
        top_artist = full[category].value_counts().nlargest(n)
        px.bar(top_artist, title='Top ' + str(n) +  ' Most Common ' +  str(category) + ' of the Decade', height=600).show()

# Top Spotify listeners
px.bar(full.user_id.value_counts().nlargest(20), title='Top Spotify Listeners', height=800)

# What artists did the top listener like
top_listener_artists = pd.DataFrame(full.query("user_id == '4398de6902abde3351347b048fcdc287'")['artist_name'].value_counts().nlargest(10))

# favorite artists of the top listener
px.pie(data_frame=top_listener_artists, values=top_listener_artists['count'], 
names=top_listener_artists.artist, hover_name=top_listener_artists.artist, 
title='Favorite 10 Artists of Top Listener', height=700)

#------------------------------------#


# Top 10 dataset
url2 = 'https://raw.githubusercontent.com/dataPracticum/codepudding/main/spotify/top_by_year/top10s.csv'
top10 = pd.read_csv(url2, encoding='latin-1')

top10.rename(columns={'top genre': 'genre'}, inplace=True)
top10 = top10.drop('Unnamed: 0', axis=1)

# Artist Popularity Based on Year
px.histogram(top10, y='pop', x='artist', color='year', title='Artist Popularity Based on Year')

# most popular artist of n year
year = top10.year.unique()
for i in year:
    yr = top10[top10.year.isin([i])]
    px.histogram(yr, y='pop', x='artist', title='Most Popular Artists of ' + str(i), height=800).show()

# top n artist of the decade
number = [5, 10, 20, 50, 100]
for n in number:
    top_artist = top10.artist.value_counts().nlargest(n)
    px.bar(top_artist, title='Top ' + str(n) +  ' Artists of the Decade', height=600).show()


# top n genres of the decade
number = [5, 10, 15, 20, 50]
for n in number:
    top_genre = top10.genre.value_counts().nlargest(n)
    px.bar(top_genre, title='Top ' + str(n) +  ' Genres of the Decade', height=600).show()

# Years with most popular songs
top_year = top10.year.value_counts(sort=False)
px.bar(top_year, title='Years With Most Popular Songs', height=600)

# Top category, n of the decade
category = top10.loc[:, 'bpm':'pop'].columns
num = [5, 10, 15, 20]
for i in category:
    for n in num:
        top_category = top10[i].value_counts().nlargest(n)
        px.bar(top_category, title='Top ' + str(n) + ' '+  str(i) + ' of the Decade', height=600).show()


#-----------------------------#

# Unpopular dataset
url3 = 'https://raw.githubusercontent.com/dataPracticum/codepudding/main/spotify/unpopular_songs.csv'
unpopular = pd.read_csv(url3)
unpopular.drop('track_id', axis=1, inplace=True)
unpopular


