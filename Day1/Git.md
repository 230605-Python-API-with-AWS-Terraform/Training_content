**What is a version control system?**

A version control system (VCS) tracks changes to a file or set of files over time. The most common type is a centralized VCS, which uses a server to store all the versions 
of a file. Developers can check out a file from the server,make changes, and check the file back in. The server then stores the new version of the file.

**What are the main version control systems?**

The three most well-known version control tools (also known as revision control systems) are Git, Subversion, and Mercurial.

`Git`
Git is the most popular option and has become synonymous with "source code management." Git is an open source distributed system that is used for software projects of any 
size, making it a popular option for startups, enterprise, and everything in between.

`Subversion (SVN)`
SVN is a widely adopted centralized VCS. This system keeps all of a project's files on a single codeline making it impossible to branch, so it's easy to scale for large 
projects. It's simple to learn and features folder security measures, so access to subfolders can be restricted.

`Mercurial`
Mercurial is a distributed VCS that offers simple branching and merging capabilities. The system enables rapid scaling and collaborative development, with an intuitive 
interface. The flexible command line interface enables users to begin using the system immediately.

**What is Git?**

Git is a version control system that you download onto your computer. It is essential that you use Git if you want to collaborate with other developers on a coding project 
or work on your own project.

In order to check if you already have Git installed on your computer you can type the command `git --version` in the terminal.

If you already have Git installed then you will see what version you have.

**What is GitHub?**

GitHub is a product that allows you to host your Git projects on a remote server somewhere (or in other words, in the cloud).

It's important to remember that GitHub is not Git. GitHub is just a hosting service. There are other companies who offer hosting services that do the same thing as 
GitHub, such as Bitbucket and GitLab.

**What is a Git Repository?**

The repository is the .git folder inside our project folder. It will track all the changes made to the files in our project and record that history over time.

The repository that we have on our computer is referred to as the local repository.

Earlier we mentioned hosting services such as GitHub, GitLab and Bitbucket. When we push (in other words upload) our local repository to one of these services, then 
the repository that resides in these service in the cloud is referred to as the remote repository.

It is important to use a remote repository in order to be able to collaborate with other people as well as to backup our projects in case something happens to our laptop or computer.

**How Does Git Track Changes?**

In order to save different versions of our project in Git we will make commits.

**What is a Git Commit?**

A commit is a version of your project. It represents a standalone version of your project and has a reference to all the files and folders that are a part of that 
version.

**How Do I Make a Commit in Git?**

In order to understand how we make a commit we need to learn about three different spaces inside Git — the working directory, staging area, and commit history.

The working directory is basically represented by the contents of our project folder (hint: a directory is the same thing as a folder). It is sort of like a work bench,
where we can add, edit, and delete files in our project.

The staging area and commit history are part of our repository.

The staging area is sort of like a rough draft space. It is where we can add updated versions of files or remove files in order to choose what we want to include in 
our next commit (version of our project). In the .git folder the staging area is represented by a file called index.

And finally the commit history is basically where our commits live after they’ve been made. In the .git folder the commit history is represented by a folder called 
objects.

**What is Git Bash?**

Git Bash is a command-line interface tool that provides a Unix-like shell environment on Windows. It allows you to interact with Git repositories and execute Git 
commands using a terminal window

