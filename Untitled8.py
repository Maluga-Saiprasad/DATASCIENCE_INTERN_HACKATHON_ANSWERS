#!/usr/bin/env python
# coding: utf-8

# In[10]:


extract_path = r"C:\Users\saivi\Downloads\movie_data\movies.csv"


# In[29]:


import pandas as pd
df_movies = pd.read_csv(extract_path)


# In[37]:


df_movies.columns


# In[20]:


df.shape


# In[16]:


r_P = r"C:\Users\saivi\Downloads\movie_data\ratings.csv"


# In[31]:


df_rating = pd.read_csv(r_P)


# In[32]:


df_rating


# In[21]:


df1.shape


# In[27]:


df1["userId"].nunique()


# In[45]:


df_movie_rating = df_movies.merge(df_rating,on = "movieId")
df_movie_rating


# In[38]:


df_movie_rating.columns


# In[42]:


grouped_data = df_movie_rating.groupby(['title', 'userId'])['rating']



# In[43]:


grouped_data.groups


# In[46]:


df_movie_rating["title"].value_counts()


# In[47]:


df_tag =r"C:\Users\saivi\Downloads\movie_data\tags.csv"


# In[48]:


df_tags = pd.read_csv(df_tag)


# In[49]:


df_tags


# In[53]:


df_merge_movie = df_movies.merge(df_tags,on = "movieId")


# In[54]:


df_merge_movie


# In[55]:


df_merge_movie.shape


# In[56]:


import pandas as pd
matrix_tags = df_merge_movie[df_merge_movie['title'] == 'Matrix, The (1999)']

selected_tags = matrix_tags['tag'].unique()
print("Tags submitted for 'Matrix, The (1999)':", selected_tags)


# In[57]:


df[df_movie_rating["title"] == 'Terminator 2: Judgment Day (1991)'].mean()


# In[58]:


import pandas as pd

# Assuming you have a DataFrame named 'df' with relevant columns
# Adjust column names accordingly

# Filter the DataFrame to include only rows for "Terminator 2: Judgment Day (1991)"
terminator_ratings = df_movie_rating[df_movie_rating['title'] == 'Terminator 2: Judgment Day (1991)']

# Calculate the average user rating
average_rating = terminator_ratings['rating'].mean()

# Display the result
print("Average user rating for 'Terminator 2: Judgment Day (1991)':", average_rating)


# In[75]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Assuming you have a DataFrame named 'df' with relevant columns
# Adjust column names accordingly

# Filter the DataFrame to include only rows for "Fight Club (1999)"
fight_club_ratings = df_movie_rating[df_movie_rating['title'] == 'Fight Club (1999)']

# Plot a histogram of user ratings
plt.figure(figsize=(10, 6))
sns.histplot(fight_club_ratings['rating'], bins=10, kde=True)
plt.title('Distribution of User Ratings for Fight Club (1999)')
plt.xlabel('User Ratings')
plt.ylabel('Frequency')
plt.show()


# In[60]:


rating_group = df_movie_rating.groupby("movieId")['rating'].agg(['count','mean'])


# In[61]:


rating_group


# In[63]:


movie_data = df_movie_rating.merge(rating_group,on="movieId")


# In[64]:


movie_data


# In[65]:


movie_data.loc[movie_data["count"]>50]


# In[67]:


import pandas as pd

# Assuming you have a DataFrame named 'df' with relevant columns including 'movieId' and 'imdbRating'
# Adjust column names accordingly

# Find the movie with the highest IMDb rating
max_imdb_rating_movie = movie_data_imbd.loc[movie_data_imbd['rating'].idxmax()]

# Extract the movieId from the result
highest_imdb_rating_movieId = max_imdb_rating_movie['movieId']

# Display the result
print("MovieId of the movie with the highest IMDb rating:", highest_imdb_rating_movieId)


# In[68]:


links_df = pd.read_csv(r"C:\Users\saivi\Downloads\movie_data\links.csv")


# In[69]:


links_df


# In[72]:


movie_data_imbd = movie_data.merge(links_df,on="movieId")


# In[73]:


movie_data_imbd


# In[74]:


movie_data_imbd.loc[movie_data_imbd["count"]>50]


# In[ ]:


rating =[]
import requests
import numpy as np
from bs4 import BeautifulSoup
for i in df_rat["imdbid"]:
    id = str(int(i))
    n_zeroes = 7 - len(id)
    new_id = "0"*n_zeroes + id
    URL = f"https://www.imdb.com/title/tt%7Bnew_id%7D/"
    request_header = {'Content-Type': 'text/html; charset=UTF-8', 
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
                      'Accept-Encoding': 'gzip, deflate, br'}
    response = requests.BeautifulSoup(URL, headers=request_header)
    soup =respone(response.text)
    imdb_rating = soup.find('div',attrs={'class':'sc-f056af46-3 dzYxjh'})
    if imdb_rating:
        rating.append(imdb_rating.text)
    else:
         rating.append(np.nan)

