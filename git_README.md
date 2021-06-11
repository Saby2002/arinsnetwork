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

	

	





