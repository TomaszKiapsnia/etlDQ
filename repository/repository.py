import git
from git import Repo
import os.path

#  TODO move to conf file
c_repo_dir = 'F:\\test'


class Repos:
    def __init__(self, git_url, repo_dir):
        if os.path.isdir(repo_dir + '\\.git'):
            g = git.cmd.Git(repo_dir)
            g.pull()
        else:
            Repo.clone_from(git_url, repo_dir)


if __name__ == '__main__':
    r = Repos('git@github.com:TomaszKiapsnia/dqtest.git', c_repo_dir)