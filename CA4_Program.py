# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:02:01 2017

@author: Jay Monpara
Student ID - 10360474
Email - 10360474@mydbs.ie

This is a program for transforming a large data set of over 5000 lines from .txt file into an organised format such as Excel or .CSV file.
Statistical calculation for analysis also done in the program.

"""

# create Commit class and define each commits as an object with details as each variable.
class Commit(object):
    
    def __init__(self, revision, author, date, time, number_of_lines, changed_path=[], comment=[], m_paths=[], a_paths=[], d_paths=[]):
        self.revision = revision
        self.author = author
        self.date = date
        self.time = time
        self.number_of_lines = number_of_lines
        self.changed_path = changed_path
        self.comment = comment
        self.m_paths = m_paths
        self.a_paths = a_paths
        self.d_paths = d_paths

    # define a function to create printable representation of the object
    def __repr__(self):
        return self.revision + ',' + self.author + \
                ',' + self.date + ',' + self.time + ',' +\
                str(len(self.m_paths)) + ',' + str(len(self.a_paths)) + ',' + str(len(self.d_paths)) + ',' + str(self.number_of_lines) + \
            ',' + ' '.join(self.comment) + '\n'

# creating function to get commits as an array
class Process_Commit(object):

    def get_commits(self, data):
        sep = 72*'-'    # setting marker between two commits
        commits = []    # initiating 'commits' array
        index = 0
        while index < len(data):
            try:
                # parse each of the commits and put them into a list of commits
                details = data[index + 1].split('|')
                # the author with spaces at end removed.
                commit = Commit(details[0].strip(),
                    details[1].strip(),
                    details[2].strip().split()[0],
                    details[2].strip().split()[1],
                    int(details[3].strip().split()[0])) # extract the digit to find no. of lines in comments
                change_file_end_index = data.index('', index + 1)   # finding new index at next empty space
                commit.changed_path = data[index + 3 : change_file_end_index] # find the array for total number of changed paths
               
                # find the total number of added, deleted and modified lines in a commit
                commit.m_paths = filter(lambda x:x == 'M', (line.split()[0] for line in commit.changed_path))
                commit.a_paths = filter(lambda x:x == 'A', (line.split()[0] for line in commit.changed_path))
                commit.d_paths = filter(lambda x:x == 'D', (line.split()[0] for line in commit.changed_path))
                commit.comment = data[change_file_end_index + 1 : 
                        change_file_end_index + 1 + commit.number_of_lines]
                # add details to the list of commits.
                commits.append(commit)
                index = data.index(sep, index + 1)
                
            except IndexError:
                index = len(data)
        return commits
    
    # create read file function and strip the white spaces from the lines
    def read_file(self, any_file):
        # use strip to strip out spaces and trim the line.
        return [line.strip() for line in open(any_file, 'r')]
    
    # create function to save commits and write the headings for an outfile
    def save_commits(self, commits, any_file):
        my_file = open(any_file, 'w')
        my_file.write("Revision,Author,Date,Time,Total_M,Total_A,Total_D, No.Of Lines, Comment\n")
        for commit in commits:
            my_file.write(str(commit))
        my_file.close()
    
    # Create functions to get total number of modifications done in the dataset.  
    def get_total_modification(self, commits):
        Total_Modifications = reduce(lambda x,y : x + y, (len(commit.m_paths) for commit in commits))
        return Total_Modifications
    
    # Create functions to get total number of amendments done in the dataset. 
    def get_total_amendments(self, commits):
        Total_Amendments = reduce(lambda x,y : x + y, (len(commit.a_paths) for commit in commits))
        return Total_Amendments
    
    # Create functions to get total number of deletions done in the dataset. 
    def get_total_deletions(self, commits):
        Total_Deletions = reduce(lambda x,y : x + y, (len(commit.d_paths) for commit in commits))
        return Total_Deletions
        
    # creating function to count number of commits by author
    def get_commits_author(self, commits, author):
        author_commits = []
        for commit in commits:
            if commit.author == author:
                author_commits.append(commit)
        return author_commits

    # Create function to get total number of authors in the data set
    def get_total_no_of_authors(self, commits):
        authors = []
        for commit in commits:
            author = commit.author
            if author not in authors:
                authors.append(author)
        return authors
        
# write main function for data transformation
if __name__ == '__main__':
    # open the file - and read all of the lines.
    process = Process_Commit()
    changes_file = 'CA-4.txt'
    data = process.read_file(changes_file)
    print len(data) #   gets length of dataset
    commits = process.get_commits(data)
    print len(commits) #total number of commits in the data
    print commits[421]  # print commit with index 421
    print commits[0]
    print len(commits[0].a_paths)   # print total number of added paths in commit with index 0.
    print 'Total Modifications = ' + str(process.get_total_modification(commits)) # printing total number of modifications
    thomas_commits = process.get_commits_author(commits, 'Thomas')
    thomas_modification = process.get_total_modification(thomas_commits)
    
    # Save file as .csv
    process.save_commits(commits, 'changes.csv')
#-------------------------------------------------------------------------------------------------------------------    
#Statistical teting for analysis of the data set.
    
 # counting number of authors  who contributed in changing paths in the data set.
    authors = []
    for commit in commits:
        author = commit.author
        if author not in authors:
            authors.append(author)
    print 'The list of authors who have contributed in changing paths is # ', authors
    print 'Total ', len(authors), ' authors have contributed in changinng the paths.'
                
    # Total number of commits made by 'Thomas'
    Thomas_commits = []
    for commit in commits:
        if commit.author == 'Thomas':
            Thomas_commits.append(commit)
    print 'Total commits made by Thomas is  = ', len(Thomas_commits)
    
    ## Total Modifications done by Thomas
    Thomas_Modifications = str(reduce(lambda x,y : x + y, (len(commit.m_paths) for commit in Thomas_commits)))
    print 'Total Modifications done by Thomas = ', Thomas_Modifications
    
    ## Total Commits made by author 'Jimmy'
    Jimmy_commits = []
    for commit in commits:
        if commit.author == 'Jimmy':
            Jimmy_commits.append(commit)
    print 'Total commits made by Jimmy is  = ', len(Jimmy_commits)
    
    
    ## Total Modifications done by Jimmy
    Jimmy_Amendments = str(reduce(lambda x,y : x + y, (len(commit.a_paths) for commit in Jimmy_commits)))
    print 'Total Amendments done by Jimmy = ', Jimmy_Amendments
    
    
    
    
    
        

 
            
            
    
             
            
        
    
        
       
        
        
        