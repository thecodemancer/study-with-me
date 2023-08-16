# Hands-on Introductory Class on Git

## Introduction

Git is a version control system that helps you track changes to your code over time. It is a powerful tool that can help you collaborate with others on projects, revert to previous versions of your code, and test new changes without affecting your main codebase.

In this class, we will learn the basics of git by creating a new repository, adding files, making changes, and committing those changes. We will also learn how to push our changes to a remote repository on GitHub.

## Prerequisites

You should have a basic understanding of the command line before taking this class. If you are not familiar with the command line, there are many resources available online that can teach you the basics.

## Getting Started

The first step is to install git on your computer. You can find installation instructions for your operating system on the [git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Once git is installed, you can create a new repository by running the following command:

```git init```

This will create a new directory called *.git* in the current directory. This directory contains all of the information about your repository, including your commit history and the list of files that have been added to the repository.

## Adding Files
To add a file to your repository, you can run the following command:

```git add filename```

This will add the file to the staging area, which is a temporary area where you can collect changes before committing them to the repository.

You can also add multiple files to the staging area by using the ```git add *``` command. This will add all of the files in the current directory to the staging area.

## Making Changes
Once you have added the files that you want to change to the staging area, you can make changes to those files. When you are finished making changes, you can commit those changes to the repository by running the following command:

```git commit -m "Your commit message"```

The *-m* flag specifies the commit message, which is a brief description of the changes that you made.

## Pushing Changes to GitHub
If you want to share your changes with others, you can push them to a remote repository on GitHub. To do this, you first need to create a GitHub account. Once you have created an account, you can create a new repository on GitHub.

To push your changes to GitHub, you can run the following command:

```git push origin master```

The origin parameter specifies the remote repository, and the master parameter specifies the branch that you want to push your changes to.

## Keep your local Git repository up-to-date with the latest changes from a remote repository.

Use the ```git fetch``` command. This command will download the latest objects, commits, and refs from the remote repository into your local repository. **It will not merge** the changes into your working directory, but it will create new remote-tracking branches that point to the fetched commits. This will allow you to see what changes have been made to the remote repository without actually updating your local working directory.

## Conclusion
In this class, we learned the basics of git by creating a new repository, adding files, making changes, and committing those changes. We also learned how to push our changes to a remote repository on GitHub.

Git is a powerful tool that can help you collaborate with others on projects, revert to previous versions of your code, and test new changes without affecting your main codebase. I encourage you to learn more about git and use it to manage your code.