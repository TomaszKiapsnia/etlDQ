import os.path
import json

#  TODO move to conf file
c_repo_dir = 'F:\\test'


class Metric:
    def __init__(self, filename):
        if os.path.isfile(c_repo_dir + '\\metrics\\' + filename + '.txt'):
            f = open(c_repo_dir + '\\metrics\\' + filename + '.txt', 'r')
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
    def __init__(self, metric1, metric2):
        self.metric1 = metric1
        self.metric2 = metric2


if __name__ == '__main__':
    m1 = Metric('metric1')
    m2 = Metric('metric2')
    m3 = Metric('metric3')
