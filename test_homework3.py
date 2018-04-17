
# coding: utf-8

# (5 points). Create a python module named test_homework3.py that tests the code in homework3.py. Write at least 3 tests (e.g., checking column names, number of rows, and verifying which columns constitute a key). Also, write a test to check that the correct exception is generated when an invalid path is provided.

# In[2]:
'''

def create_dataframe(file_path):
    import pandas as pd
    import sqlite3
    import os
    if not os.path.exists(file_path):
        raise ValueError('The file path is not valid') 
    data = sqlite3.connect(file_path)
    global df
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


# In[4]:


create_dataframe('class.db')

'''
# In[5]:


import unittest
from homework3 import create_dataframe

class TestCreateDatabase(unittest.TestCase):

    def test_columnnames(self):
        columns = create_dataframe('class.db').columns
        condition = (len(columns) == 3 and
                 'category_id' in columns and
                 'video_id' in columns and
                 'language' in columns)
        self.assertTrue(condition)
        
    def test_keys(self):
        df_distinct = create_dataframe('class.db').groupby(['video_id','language']).nunique()
        self.assertTrue(len(set(df_distinct['category_id'])) == 1)
        
    
    def test_rows(self):
        self.assertTrue(create_dataframe('class.db').shape[0] > 10)
    
    def test_file_path(self):
        import os
        self.assertRaises(ValueError,create_dataframe,'not_a_file_path')

if __name__ == '__main__':
    unittest.main()

    '''
suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateDatabase)
_ = unittest.TextTestRunner().run(suite)
'''

