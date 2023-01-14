# Project instructions

This task is to create a program that prints specific facts about a local git repository.

## Input:

    git_dir: directory in which to assess git status

## Output:

    - active branch
    - whether repository files have been modified (boolean)
    - whether the current head commit was authored in the last week (boolean)
    - whether the current head commit was authored by Rufus (boolean)

## Sample Output Format
    - active branch: master
    - local changes: False
    - recent commit: True
    - blame Rufus: True

## Instructions
    1. Run "pip install -r requirements.txt" 
    2. Run "python print_git_info.py" and input the git_dir.
