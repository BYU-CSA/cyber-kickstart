# How to add to this repository
You're going to need 2 things:
- Command line with `git` installed
- Some resources to add or ideas to edit the repository

`git` is a tool that does "version management". Practically everyone uses it to manage multiple people editing the same source code. You're going to "clone" the main repository (or "repo") down, then create a "branch" with your changes, "commit" your "staged" changes, "push" your commits, then "merge" it into the main "branch". If you can explain all of those terms in quotes, you'll know as much about git as your average Software Engineer.

To get a command line with git on Windows, download [Git Bash](https://git-scm.com/downloads), a command line program for Windows that mimics a Linux command line. When using this program, you'll use Linux commands like `ls` and `cd` instead of Windows commands like `dir` and `chdir`. Git is packaged with this program.

1. Find a spot to clone this repository. Typically, people have a directory called "CTF" or "Cyber" where they put everything.
2. In command line, navigate to the directory where you're going to clone this repository with `cd` and run `git clone https://github.com/BYU-CSA/cyber-kickstart.git`.
3. Run `cd cyber-kickstart` to change the current directory to the repo. You are now "in" the repo. As long as you're "in" the repo, the `git` command will know that you're trying to make changes to this repo, and that it's originally hosted on github.
4. Run `git checkout -b <branch-name>`. Make `<branch-name>` something short and descriptive preferably starting with your name, like `jake-mullins-sql-injection-resources` or `macen-bird-notes-dump`. If you're editing a lesson, it's fine to just say `cryptography-lesson-edits` or something similar.
5. Open the repository in your preferred editor and make your changes. Make sure to consult the `README.md` for where to put certain things. Almost everything is in Markdown, a simple language that does simple formatting. Most people use VSCode now, where you can preview your work using a Markdown preview extension.
6. Run `git status` to see which files have been changed, and run `git add <files>` to stage your changes.
7. Run `git commit -m "<commit message>"` to commit your staged changes to the branch, substituting `<commit message>` with a simple message on what was changed in this commit, like `Cloud + SOC resources` or `Cryptography lesson updates`.
8. Push your changes to the new branch with `git push`. You'll probably need to set your name and email in your command line so that Github knows who committed the changes. You can verify that a new branch was created by looking at the repository on the Github website [here](https://github.com/BYU-CSA/cyber-kickstart.git), and clicking "branches".
9. When you're ready to officially add your resources to the main branch for everyone else, make a Pull Request on the Github website.
10. Send a message over slack to someone with permission to merge your resources to look over your Pull Request.
11. Celebrate! You've just contributed to making Cybersecurity education free-er and more approachable for anyone with an internet connection. Happy Hacking!

![Git branches flow](https://media.licdn.com/dms/image/D5612AQF1IBC1zNxOfA/article-cover_image-shrink_600_2000/0/1708253182849?e=2147483647&v=beta&t=QcXFNFet6jFw1L5EksukfuYTqtbCrZzhdMUtWv8MNYE)

![Git branches merge](https://www.nobledesktop.com/image/gitresources/git-branches-merge.png)
