import datetime

class LogFormatter(object):

    @staticmethod
    def process_line(line):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M') + '  ' + line + '\n'


class CSVFormatter(object):

    @staticmethod
    def process_line(line):
        updated = []
        for item in line:
            if item.find(',') == -1:
                updated.append(item)
            else:
                updated.append('"' + item + '"')
        return ",".join(updated) + '\n'


class WriteFile(CSVFormatter, LogFormatter):
    def __init__(self, filename, cls):
        self.cls = cls
        self.fh = open(filename, 'a')

    def write(self, input_line):
        self.fh.write(self.cls.process_line(input_line))

    def close(self):
        self.fh.close()

