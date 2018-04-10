import datetime
import abc

class WriteFile(object):
    def __init__(self, file, delim=','):
        self.file = file
        self.delim = delim

    def to_file(self):
        fh = open(self.file, 'a')
        fh.write(self.output_line)
        fh.close()

    @staticmethod
    def log_date():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    @abc.abstractmethod
    def write(self, line):
        "Write a line of input, processed in the correct way to file"
        return


class DelimFile(WriteFile):

    def write(self, line):
        self.output_line = ",".join(line) + '\n'
        self.to_file()


class LogFile(WriteFile):

    def write(self, line):
        self.output_line = self.log_date() + '  ' + line + '\n'
        self.to_file()
