# challenge

Git Commit Correct File
In the Bash script, write a simple set of Git commands to do the following:

First, clone the repository located at https://github.com/coderbyte-org/big-o. Move into the project directory, create, and switch to a new branch called feat/add-correct-file.

Next, create two files: file-1.txt and file-2.txt. Add file-2.txt to the staging area and commit the changes with the message feat: add correct file

Finally, print the results of:

git status && git log -1 --pretty=format:'' --stat

<!--
#!/bin/bash
git clone http://github.com/coderbyte-org/big-o
cd big-o
git branch feat/add-correct-file
touch file-1.txt
touch file-2.txt
git add file-2.txt
git commit -m "feat: add correct file"
git status && git log -1 --pretty=format:'' --stat
-->
