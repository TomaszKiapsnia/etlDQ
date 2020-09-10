import git
import json
from git import Repo
import os.path

def load_repo_dir():
    if os.path.isfile('../conf.json'):
        f = open('../conf.json', 'r')
        txt = f.read()
        f.close()
        conf = json.loads(txt)
        return conf['repo_dir']


class Repos:
    def __init__(self, git_url, repo_dir):
        if os.path.isdir(repo_dir + '\\.git'):
            g = git.cmd.Git(repo_dir)
            g.pull()
        else:
            Repo.clone_from(git_url, repo_dir)


if __name__ == '__main__':
    r = Repos('git@github.com:TomaszKiapsnia/dqtest.git', load_repo_dir())