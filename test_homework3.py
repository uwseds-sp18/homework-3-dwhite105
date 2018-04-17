
# coding: utf-8

# (5 points). Create a python module named test_homework3.py that tests the code in homework3.py. Write at least 3 tests (e.g., checking column names, number of rows, and verifying which columns constitute a key). Also, write a test to check that the correct exception is generated when an invalid path is provided.




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
        df = create_dataframe('class.db')
        df_dup = df.drop_duplicates(['language','video_id'])
        self.assertTrue(df_dup.shape[0] == df.shape[0])
        
    
    def test_rows(self):
        df = create_dataframe('class.db')
        self.assertTrue(df.shape[0] > 10)
    
    def test_file_path(self):
        self.assertRaises(ValueError,create_dataframe,'not_a_file_path')

if __name__ == '__main__':
    unittest.main()

