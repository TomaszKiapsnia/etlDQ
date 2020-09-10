import os.path
import json


def load_repo_dir():
    if os.path.isfile('conf.json'):
        f = open('conf.json', 'r')
        txt = f.read()
        conf = json.loads(txt)
        f.close()
        return conf['repo_dir']


class Metric:
    ''' keep results of SQL from database.
    TODO
    1. read SQL
    2. execute SQL on DB
    3. keep result
    4. compare more complex situations, when sql returns more than 1 value
    '''
    def __init__(self, filename):
        repo_dir = load_repo_dir()
        if os.path.isfile(repo_dir + '\\metrics\\' + filename + '.txt'):
            f = open(repo_dir + '\\metrics\\' + filename + '.txt', 'r')
            self.metric_value = int(f.read())
            f.close()
        else:
            pass

    def __eq__(self, other):
        return self.metric_value == other.metric_value

    def __ne__(self, other):
        return self.metric_value != other.metric_value

    def __gt__(self, other):
        return self.metric_value > other.metric_value

    def __lt__(self, other):
        return self.metric_value < other.metric_value

    def __ge__(self, other):
        return self.metric_value >= other.metric_value

    def __le__(self, other):
        return self.metric_value <= other.metric_value


class Test:
    ''' connects two metrics to compare '''
    def __init__(self, metric1, metric2):
        self.metric1 = metric1
        self.metric2 = metric2

    def execute(self):
        return self.metric1 == self.metric2


if __name__ == '__main__':
    m1 = Metric('metric1')
    m2 = Metric('metric2')
    m3 = Metric('metric3')

    t1 = Test(m1, m2)
    t2 = Test(m1, m3)
    print(t1.execute())
    print(t2.execute())
