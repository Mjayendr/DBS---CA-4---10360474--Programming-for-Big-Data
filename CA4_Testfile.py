# -*- coding: utf-8 -*-
"""
@author: Jay Monpara
Student ID - 10360474
Email - 10360474@mydbs.ie
"""
import unittest
from CA4_Program import read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('CA-4.txt')
    
    # Test total number of lines in the text file
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    # Test number of commits in the file
    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
        
        #testing for author name for first commit 
        self.assertEqual('Thomas', commits[0].author)
        
        # testing for author name in 420th commit
        self.assertEqual('Jimmy', commits[420].author)
        
        # tesing for comment details for commit 24.
        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
                'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
                commits[24].comment)
        
        # Testing for details of changed path for commit 20
        self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],
                commits[20].changed_path)
        
        

if __name__ == '__main__':
    unittest.main()

