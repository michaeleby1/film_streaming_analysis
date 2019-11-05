import pandas as pd 
import numpy as np

df_title = pd.read_table('title.basics.tsv.gz')
df_ratings = pd.read_table('title.ratings.tsv.gz')
df_name = pd.read_table('name.basics.tsv.gz')

na_dict = {'\\N': np.nan}

df_movies = df_title[df_title['titleType'] == 'movie']
df_movies.drop(['titleType', 'originalTitle', 'isAdult', 'endYear'], axis=1, inplace=True)
df_movies = df_movies.rename(columns={'startYear': 'year', 'runtimeMinutes': 'runtime', 'primaryTitle': 'title'})
df_movies['year'] = df_movies['year'].replace(na_dict)
df_movies.dropna(subset=['year'])
df_movies['year'] = pd.to_numeric(df_movies['year'])

df_movies = df_movies.set_index('tconst').join(df_ratings.set_index('tconst'))
df_movies = df_movies.reset_index()

df_imdb_names = df_name.drop('knownForTitles', axis=1)
df_imdb_names['deathYear'] = df_imdb_names['deathYear'].replace(na_dict)
df_imdb_names['birthYear'] = df_imdb_names['birthYear'].replace(na_dict)
df_imdb_names = df_imdb_names.dropna(subset=['birthYear'])
df_imdb_names = df_imdb_names.dropna(subset=['primaryProfession'])