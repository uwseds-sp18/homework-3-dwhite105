
# coding: utf-8

# (2 points). Create a python module named homework3.py that provides the same capabilities as create_dataframe in homework 2, and also checks that there is a valid path to the database (the function argument). If the path is not valid, a ValueError exception is raised.

# In[34]:


def create_dataframe(file_path):
    import pandas as pd
    import sqlite3
    import os
    if not os.path.exists(file_path):
        raise ValueError('The file path is not valid') 
    data = sqlite3.connect(file_path)
    #global df
    df = pd.read_sql_query(""" SELECT category_id, video_id, 'ca' as language
    FROM CAvideos
    UNION
    SELECT category_id, video_id, 'fr' as language
    FROM FRvideos
    UNION
    SELECT category_id, video_id, 'de' as language
    FROM DEvideos
    UNION
    SELECT category_id, video_id, 'gb' as language
    FROM GBvideos
    UNION
    SELECT category_id, video_id, 'us' as language
    FROM USvideos;""", data)
    data.close()
    return df


# In[35]:


create_dataframe('class.db')

