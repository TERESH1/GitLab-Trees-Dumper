import os

class Detector:
    def __init__(self, title, *ext):
        self.title = title
        self.ext = ext
        self.found = False
        self.filename = 'logs/' + title + '.log'
        
    def Check(self, file_path, log_to_file = True):
        if not file_path.endswith(self.ext): return
        if not self.found:
            self.found = True
            if log_to_file:
                with open(self.filename, 'w') as f:
                    print(file_path, file=f)
        elif log_to_file:
            with open(self.filename, 'a') as f:
                print(file_path, file=f)
        print(f'{file_path}: {self.title}')
        

class Checker:
    def __init__(self, log_to_file = True):
        self.exts = ()
        self.detectors = []
        if log_to_file and not os.path.exists('logs'):
            os.makedirs('logs')
    
    def Add(self, title, *ext):
        self.detectors.append(Detector(title, *ext))
        self.exts += ext
        
    def Check(self, file_path, log_to_file = True):
        if not file_path.endswith(self.exts):
            print(f'{file_path}: Unknown')
            return
        for detector in self.detectors:
            detector.Check(file_path, log_to_file)
