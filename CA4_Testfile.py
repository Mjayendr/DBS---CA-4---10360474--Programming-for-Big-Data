# -*- coding: utf-8 -*-
"""
@author: Jay Monpara
Student ID - 10360474
Email - 10360474@mydbs.ie
"""
import unittest
from CA4_Program import Process_Commit

class TestCommits(unittest.TestCase):
    
         
    def setUp(self):
        self.process = Process_Commit()
        self.data = self.process.read_file('CA-4.txt')
        self.commits = self.process.get_commits(self.data)
        
        
    # Test total number of lines in the text file
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))
    
    def test_total_modification(self):
        self.assertEqual(1186, self.process.get_total_modification(self.commits))
    
    def test_total_amendments(self):
        self.assertEqual(1056, self.process.get_total_amendments(self.commits))
        
    def test_total_deletions(self):
        self.assertEqual(767, self.process.get_total_deletions(self.commits))

    # Test number of commits in the file
    def test_number_of_commits(self):
        self.assertEqual(422, len(self.commits))
        
        #testing for author name for first commit 
    def test_author_for_commits(self):
        self.assertEqual('Thomas', self.commits[0].author)
        # testing for author name in 420th commit
        self.assertEqual('Jimmy', self.commits[420].author)
        
        # tesing for comment details for commit 24.
    def test_comments_for_commits(self):
        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
                'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
                self.commits[24].comment)
        # Testing for details of changed path for commit 20
        self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],
                self.commits[20].changed_path)
    
    def test_no_of_commits_by_Thomas(self):
        self.assertEqual(191, len(self.process.get_commits_author(self.commits, 'Thomas')))
        
        
    def test_total_number_of_authors(self):
        self.assertEqual(10, len(self.process.get_total_no_of_authors(self.commits)))
        
if __name__ == '__main__': 
    unittest.main()
