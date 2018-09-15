# Git Dated Commit

## What
A Python script to commit all files in a directory with their file modification times.

## Usage
### Requirements
1. [dateutil](https://dateutil.readthedocs.io/en/stable/index.html). Install using pip:
```
pip install python-dateutil
```

### How to use
```
usage: python dated_commit.py [-h] path

positional arguments:
  path        Path to the folder containing files to commit

optional arguments:
  -h, --help  show this help message and exit
```

## Why
I wanted to create a git repository for an already existing project. I also wanted to preserve some form of history for the project. By committing all the files with their modified times, I can see the last time I touched a file. I can also see approximately when I started my project. I couldn't find a solution that does this, so I created one myself :) .

## Resources
- [How to work with dates and time with Python](https://web.archive.org/web/20180915081950/https://opensource.com/article/17/5/understanding-datetime-python-primer)
- [Interacting with GitHub Using Python](https://web.archive.org/web/20180914122317/https://www.ivankrizsan.se/2017/03/19/interacting-with-github-using-python/)
- [Git Internals - Environment Variables](https://web.archive.org/web/20180915082510/https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables)
- [Making Git Commits in the Past](https://web.archive.org/web/20180915083045/https://leewc.com/articles/making-past-git-commits/)
- [Working with dates in Git](https://web.archive.org/web/20180915083017/https://alexpeattie.com/blog/working-with-dates-in-git)
