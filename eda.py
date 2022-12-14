
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

# first dataset
url1 = 'https://media.githubusercontent.com/media/dataPracticum/codepudding/main/spotify/spotify_dataset.csv'
full = pd.read_csv(url1, on_bad_lines='skip', names=[
    'user_id', 'artist_name', 'track_name', 'playlist_name'])


# artists of the decade
number = [5, 10, 20, 50, 100]
for n in number:
    top_artist = full.artist_name.value_counts().nlargest(n)
    px.bar(top_artist, title='Top ' + str(n) +
           ' Most Common Artists of the Decade', height=600, template='plotly_dark', color_discrete_sequence=['green']).show()


# artist of the decade percentage
number = [5, 10, 20]
for n in number:
    top_artist = full.artist_name.value_counts(
        normalize=True).nlargest(n) * 100
    px.bar(top_artist, title='Top ' + str(n) +
           ' Most Common Artists of the Decade as Percentage', height=600, log_y=True, template='plotly_dark', color_discrete_sequence=['green']).show()


# playlists of the decade
number = [5, 10, 15, 25]
for n in number:
    top_playlists = full.playlist_name.value_counts().nlargest(n)
    px.bar(top_playlists, title='Top ' + str(n) +
           ' Most Common Playlists of the Decade', height=600).show()


# most common artist
number = [5, 10, 20, 50, 100]
for n in number:
    top_artist = full.artist_name.value_counts().nlargest(n)
    px.bar(top_artist, title='Top ' + str(n) + ' Most Common Artists of the Decade',
           height=600, template='plotly_dark', color_discrete_sequence=['green']).show()


# most common playlist name
number = [5, 10, 20, 50, 100]
for n in number:
    top_artist = full.playlist_name.value_counts().nlargest(n)
    px.bar(top_artist, title='Top ' + str(n) + ' Most Common Playlists of the Decade',
           height=600, template='plotly_dark', color_discrete_sequence=['green']).show()


# Top Spotify listeners
px.bar(full.user_id.value_counts().nlargest(20),
       title='Top Spotify Listeners', height=800, template='plotly_dark',
       color_discrete_sequence=['green']).show()

# What artists did the top listener like
top_listener_artists = pd.DataFrame(full.query("user_id == '4398de6902abde3351347b048fcdc287'")[
                                    'artist_name'].value_counts().nlargest(10))

top_listener_artists.reset_index(inplace=True)
top_listener_artists.columns = ['artist', 'count']
top_listener_artists

# favorite artists of the top listener
px.pie(data_frame=top_listener_artists, values=top_listener_artists['count'],
       names=top_listener_artists.artist, hover_name=top_listener_artists.artist,
       title='Favorite 10 Artists of Top Listener', height=700, template='plotly_dark').show()


#------------------------------------#


# Top 10 dataset
url2 = 'https://raw.githubusercontent.com/dataPracticum/codepudding/main/spotify/top_by_year/top10s.csv'
top10 = pd.read_csv(url2, encoding='latin-1')

top10.rename(columns={'top genre': 'genre'}, inplace=True)
top10 = top10.drop('Unnamed: 0', axis=1)

# Artist Popularity Based on Year
px.histogram(top10, y='pop', x='artist', color='year',
             title='Artist Popularity Based on Year').show()


# popularity by year interactive
artist_pivot = pd.pivot_table(
    top10, index='artist', columns='year', values='pop', aggfunc='sum')
px.scatter(artist_pivot, animation_frame='year', title='Artist Popularity by Year',
           height=700, template='plotly_dark', color_discrete_sequence=['green']).show()


# artist popularity over the years
px.scatter(top10, y='pop', x='artist', animation_frame='year', size='nrgy', height=700, range_y=[
           0, 110], title='Artist Popularity Over the Years', template='plotly_dark', color_discrete_sequence=['green']).show()


# most popular artist of n year
year = top10.year.unique()
for i in year:
    yr = top10[top10.year.isin([i])]
    px.histogram(yr, y='pop', x='artist',
                 title='Most Popular Artists of ' + str(i), height=800, template='plotly_dark', color_discrete_sequence=['green']).show()

# top n artist of the decade
number = [5, 10, 20, 50, 100]
for n in number:
    top_artist = top10.artist.value_counts().nlargest(n)
    px.bar(top_artist, title='Top ' + str(n) +
           ' Artists of the Decade', height=600, template='plotly_dark',
           color_discrete_sequence=['green']).show()


# top n genres of the decade
number = [5, 10, 15, 20, 50]
for n in number:
    top_genre = top10.genre.value_counts().nlargest(n)
    px.bar(top_genre, title='Top ' + str(n) +
           ' Genres of the Decade', height=600, template='plotly_dark',
           color_discrete_sequence=['green']).show()

# Years with most popular songs
top_year = top10.year.value_counts(sort=False)
px.bar(top_year, title='Years With Most Popular Songs', height=600,
       template='plotly_dark', color_discrete_sequence=['green']).show()

# Top category, n of the decade
category = top10.loc[:, 'bpm':'pop'].columns
num = [5, 10, 15, 20]
for i in category:
    for n in num:
        top_category = top10[i].value_counts().nlargest(n)
        px.bar(top_category, title='Top ' + str(n) + ' ' +
               str(i) + ' of the Decade', height=600, template='plotly_dark', color_discrete_sequence=['green']).show()


#-----------------------------#

# Unpopular dataset
url3 = 'https://raw.githubusercontent.com/dataPracticum/codepudding/main/spotify/unpopular_songs.csv'
unpopular = pd.read_csv(url3)
unpopular.drop('track_id', axis=1, inplace=True)
unpopular


# Popularity Ratings
px.histogram(unpopular.popularity, title='Popularity Ratings', template='plotly_dark',
             color_discrete_sequence=['green']).show()


# Distribution of Explicit Songs Amongst Unpopular Tracks
px.bar(unpopular.explicit.value_counts(), color=['Explicit', 'Non Explicit'],
       title='Distribution of Explicit Songs Amongst Unpopular Tracks', template='plotly_dark', color_discrete_sequence=['green', 'white']).show()

# category for tracks in unpopular songs
category = unpopular.loc[:, 'danceability':'duration_ms'].columns
for i in category:
    px.histogram(unpopular[i], title='Distribution of ' + str.upper(i) + ' for Tracks Amongst Unpopular Songs',
                 height=600, template='plotly_dark', color_discrete_sequence=['green']).show()


# Grammys for each year
 # made from https://www.popvortex.com/music/grammy-awards/song-of-the-year.php

d = {'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
     'song': ['Single Ladies (Put a Ring on It', 'Need You Now', 'Rolling in the Deep', 'We Are Young', 'Royals',
              'Stay With Me', 'Thinking Out Loud', 'Hello', 'Thats What I Like', 'This Is America'],
     'artist': ['Beyonce', 'Lady Antebellum', 'Adele', 'Fun. Featuring Janelle Monae', 'Lorde', 'Sam Smith', 'Ed Sheeran',
                'Adele', 'Bruno Mars', 'Childish Gambino']}
grammys = pd.DataFrame(data=d)
print('Grammy Winners')
display(grammys)


# super bowl performers
# made from https://www.si.com/nfl/2019/02/03/super-bowl-halftime-performers-past-artists-all-time-list
f = {'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
     'artist': ['The Who', 'The Black Eyed Peas, Usher, Slash', 'Madonna, LMFAO, Nicki Minaj, M.I.A, Cee Lo Green',
                'Beyonce and Destinys Child', 'Bruno Mars and Red Hot Chili Peppers', 'Katy Perry, Lenny Kravitz, Missy Elliott',
                'Coldplay, Beyonce, Bruno Mars, Mark Ronson', 'Lady Gaga', 'Justin Timberlake', 'Maroon 5 with Big Boi and Travis Scott']}
super_bowl = pd.DataFrame(data=f)
print('Super Bowl Performers')
display(super_bowl)


# AMA Winners
# made from https://en.wikipedia.org/wiki/American_Music_Award_for_Artist_of_the_Year
g = {'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
     'artist_of_the_year': ['Justin Bieber', 'Taylor Swift', 'Justin Bieber', 'Taylor Swift', 'One Direction', 'One Direction',
                            'Ariana Grande', 'Bruno Mars', 'Taylor Swift', 'Taylor Swift']}
amas = pd.DataFrame(data=g)
print('American Music Award Winners')
display(amas)


# artists by total number one singles
tables = pd.read_html(URL)
table2 = tables[3]
table2.columns = ('artist', 'number_one_singles', 'singles')

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
print('Artist by Total Number-One Singles')
display(table2)

# Chart of number one singles
px.histogram(table2, x='artist', y='number_one_singles', title='Total Number-One Singles',
             height=800, template='plotly_dark', color_discrete_sequence=['green']).show()


# Artists by total cumulative weeks at number-one
tables = pd.read_html(URL)
table3 = tables[4]
table3.columns = ('artist', 'weeks_at_number_one', 'singles')
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
print('Total Cumulative Weeks at Number One')
display(table3)

# total cumulative weeks at number one
px.histogram(table3, x='artist', y='weeks_at_number_one', title='Total Cumulative Weeks at Number One',
             height=800, template='plotly_dark', color_discrete_sequence=['green']).show()


# Songs by total number of weeks at number one
tables = pd.read_html(URL)
table4 = tables[5]
table4.drop('References', axis=1, inplace=True)
table4.columns = ('song', 'artists', 'weeks_at_number_one')
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
print('Songs by Total Number of Weeks at Number One')
display(table4)


# histogram of table 4
px.histogram(table4, x='artists', y='weeks_at_number_one',
             title='Songs by Total Number of Weeks at Number One', height=800, template='plotly_dark', color_discrete_sequence=['green']).show()