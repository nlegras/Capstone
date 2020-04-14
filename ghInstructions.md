# GitHub Instructions


### Setup

1. download github scm
2. fork to personal repo (browser)
3. create local repo folder
	- cd to local repo (open with github scm)
4. clone your fork to local 
	- git clone url
	- git branch -a
	- git remote add upstream (me)
	- git checkout dev


### When we start a new feature:

1. start a new branch
	- git checkout dev
	- git pull upstream dev (mine)
	- git checkout -b feature003


### Everytime you work

1. verify local matches remote esp for different machines
	- git pull origin feature003
	- git checkout feature003


### Everytime you make a notable change that you want to save

1. edit files/do work
	- git add *
	- git commit -m "description so we all know what it is"
	- git push origin feature003 (sends changes to feature branch to make sure there are no conflicts)

2. When feature is complete, look for merge conflicts
	- git checkout dev (local dev branch)
	- git pull origin dev (remote dev)
	- git pull upstream dev (my dev)
	- git checkout feature003 (local feature branch)
	- git merge dev (local dev to local feature)

3. fix merge conflicts --> repeat 1 and 2
	- git push origin feature003

4. in browser
	- pull request your feature003 to Natalie's.


