#A read me test file 
#How to use Git

Source: https://www.youtube.com/watch?v=0fKg7e37bQE
Video Name: Github Tutorial For Beginners - Github Basics for Mac or Windows & Source Control Basics

1. Download the Github application on computer.
2. Get the "clone url" of the project repository.
3. Run Terminal / cmd: git clone "repository url".

Commands: 
git status - To check which changes have been staged, which haven't, and which files are being tracked by Git.
git add example.md - Add a file into Index, but not sync up yet OR add -A to add ALL.
git commit -m "something" - Commit all file changes after last commit, except untracked files, with   -m "something"   adding a message. (No need to connect to Internet)
git push - Update the server with your commits across all branches that are COMMON between your local copy and the server. (Need to connect to Internet)
git pull - Incorporates changes from a remote repository into the current branch.

If git commit without a message, you can use the "Esc" key then type :wq

Source: https://www.youtube.com/watch?v=SWYqp7iY_Tc
Video Name: Git & GitHub Crash Course For Beginners

Command:
git branch login - Create a branch for working on the login functionality
git checkout login -  Switch to the login branch
git merge login - Merge the login branch to Master
