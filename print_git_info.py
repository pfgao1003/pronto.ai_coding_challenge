import os
from git import Repo
import datetime
class GitInfo:
    def __init__(self, git_dir:str):
        self.repository = Repo(git_dir)

    def print_git_info(self):
        is_local_change = self.repository.is_dirty()
        is_last_week = (datetime.datetime.now().astimezone() - self.repository.head.commit.authored_datetime) < \
        datetime.timedelta(days=7)
        is_rufus = self.repository.head.commit.author.name == "Rufus"
        print("active branch: ", self.repository.active_branch.name)
        print("local changes: ", is_local_change)
        print("recent commit: ", is_last_week)
        print("blame Rufus: ", is_rufus)

if __name__ == "__main__":
    git_dir = input("Please input your git_dir: ")
    if os.path.isdir(git_dir):
        GitInfo(git_dir).print_git_info()
    else:
        raise Exception("Directory is not valid.")