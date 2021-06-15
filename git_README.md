##GIT INITIAL SETUP
- Need to specify user name & user email
	- git config --global user.name "USERNAME"
	- git config --global user.email "USERNAME@EMAIL"

## These details are stored in git config file
	- git config --list

## Initilize GIT (this will create a .git folder containing the service file)
	- git init

## Working with GIT
	- When you are working with git it is important to understand current status of repository
		- git status

	- Git status will give information of the Branch.
	- Default Master Branch is auto created and used by default
	- Git also create or copy file and then use "git add" command to start git tracking
		- git add .
	- It looks as per the below mentioned output, when I create a file name git_README.md

====================OUTPUT=============================
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.bash-git-prompt/
	git_README.md
- nothing added to commit but untracked files present (use "git add" to track)
=======================================================

	- Now files are in a section called "Changes to be committed"
         	new file:   git_README.md
	- All necessary files are added in staged, now we can commit changes to it.
		git commit -m "Version 0.0.1. Adding commit to git_README.md files"
=====================OUTPUT=============================
$ git status
On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
========================================================
	
	- "Nothing to commit", working directory clean. No changes to add to Git or to commit.

## Git Diff

- git diff command shows what change have been made since last commit
- Any changes made and statge via git add command and then run "git diff". it will show you nothing. 

- For example : I added these line GIT DIFF in this git_README.md and then git add git_README.md. This will show nothing in GIT DIFF. 

===================OUTPUT==============================
File Modified Only : 

+## Git Diff
 
+- git diff command shows what change have been made since last commit
+- Any changes made and statge via git add command and then run "git diff". it will show you nothing. 
+
+- For example : I added these line GIT DIFF in this git_README.md and then git add git_README.md. This will show nothing in GIT DIFF. 
+

Performed git add only : 

$ git add git_README.md 
$ git diff

No output in git diff. 

Now performed git commit : 

$ git commit -m "Version 0.0.2"
[master ef6cf70] Version 0.0.2
 1 file changed, 31 insertions(+), 1 deletion(-)

=====================================================

- To see the difference between staging and last commit, add parameter --staged after only git add. 

-------------------------------------------------------
$ git diff --staged
diff --git a/git_README.md b/git_README.md
index 76bb6c5..7e575d3 100644
--- a/git_README.md
+++ b/git_README.md
@@ -77,7 +77,9 @@ $ git commit -m "Version 0.0.2"
 [master ef6cf70] Version 0.0.2
  1 file changed, 31 insertions(+), 1 deletion(-)
------------------------------------------------------

## Git Log
	
- This command will give the details about the last changes made
	- git log
- By default, all the command displays all commit from the nearest time. 

===================OUTPUT================================

commit a4da7509791a809b28f86aab7f25536d09a8b9b1
Author: Saby2002 <sabyasachikar24@gmail.com>
Date:   Sat Jun 12 03:09:55 2021 +0530

    Version 0.0.2

commit e214fb7ac5aa1faea96370a4f5831c0db957e1a1 (origin/master)
Author: arin <arin@arinsnetwork.com>
Date:   Fri Jun 11 19:31:47 2021 +0530

    0.0.1
==========================================================

- Flag -p allows to give the difference that have been made by each commit.

===================OUTPUT=================================

commit 30fe5cc1968138c2df174a567b55d63b4f79c8f2 (HEAD -> master)
Author: Saby2002 <sabyasachikar24@gmail.com>
Date:   Sat Jun 12 03:25:27 2021 +0530

    Version 0.0.2

diff --git a/git_README.md b/git_README.md
index 7610abc..76bb6c5 100644
--- a/git_README.md
+++ b/git_README.md
@@ -64,6 +64,18 @@ File Modified Only :
 +- For example : I added these line GIT DIFF in this git_README.md and then git add git_README.md. This will show nothing in GIT DIFF. 
 +
 
+Performed git add only : 
+
+$ git add git_README.md 
+$ git diff
+
+No output in git diff. 
+
+Now performed git commit : 
+
+$ git commit -m "Version 0.0.2"
+[master ef6cf70] Version 0.0.2
+ 1 file changed, 31 insertions(+), 1 deletion(-)        

commit ef6cf70b698b5db51153b4153f198f595acbae3c
Author: Saby2002 <sabyasachikar24@gmail.com>
Date:   Sat Jun 12 03:23:19 2021 +0530

    Version 0.0.2
=========================================================

- Shorter output option to use flag --stat

=====================OUTPUT==============================
commit 30fe5cc1968138c2df174a567b55d63b4f79c8f2 (HEAD -> master)
Author: Saby2002 <sabyasachikar24@gmail.com>
Date:   Sat Jun 12 03:25:27 2021 +0530

    Version 0.0.2

 git_README.md | 12 ++++++++++++
 1 file changed, 12 insertions(+)

commit ef6cf70b698b5db51153b4153f198f595acbae3c
Author: Saby2002 <sabyasachikar24@gmail.com>
Date:   Sat Jun 12 03:23:19 2021 +0530

    Version 0.0.2

 git_README.md | 32 +++++++++++++++++++++++++++++++-
 1 file changed, 31 insertions(+), 1 deletion(-)

commit bf013343ab41e8d23cbca286dd2df1285181b4bf
Author: Saby2002 <sabyasachikar24@gmail.com>
Date:   Sat Jun 12 03:11:26 2021 +0530
===========================================================

## Cloning a GitHub Repository 

- To clone locally with repository, it should be cloned. 
- Use "git clone" command to clone repository 

	- git clone https://github.com/Saby2002/arinsnetwork.git

## Working with repository 

- Git clone command not only copied repository to use it locally, but also configured git accordingly. 
	- Folder .git was created
	- All repository data is downloaded
	- Downloaded all changes that were in repository 
	- GitHub repository as a remote for local repository

- Now we have the complete local Git repository where we can work. 

	- sync local content with GITHUB using git pull command
	- Modifying repository files
	- Commit changes using git commit commnd
	- Transfering local changes to GITHUB repository with git PUSH Command 
	- When working first we need to update the local repository 
	- Then we need to load changes to GIT

- Synchronizing local repository with remote repository

	- All commands are executed inside repository directory
	- If contents of local repository are the same as those of remote repository "Git pull" says upto date. 
	- if any changes were made then pull from the Github all the directories from the githun
	- If you want to add a specific file, you need to enter git. and do git add. command
	- Followed by git -m commit. Its always better to specify what you are adding or any specific version details associated with this as a form of comment. 
	- Git Push on GitHub
		- Command "git push" is used to load all local changes to GITHUB
	- Before executing git push you can run git log -p/origin. It will show what changes you are going to add to your repository on GitHub
	- 

