# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# dir
#     subdir1
#     subdir2
#         file.ext
# Given a string representing the file system in the above format, 
# return the length of the longest absolute path to a file in the 
# abstracted file system. If there is no file in the system, return 0.

import os


class File:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.path = os.path.join(parent.path if parent else '', name)


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.path = os.path.join(parent.path if parent else '', name)
        self.child_folder = []
        self.file = []

    def add_file(self, file):
        self.file.append(file)

    def add_folder(self, folder):
        self.child_folder.append(folder)


class FileSystem:
    def __init__(self, path):
        self.longest_path = ''
        self.max_depth = -1
        self.parse(path)

    def parse(self, path):
        depth = 0
        self.dir = Folder('', None)
        current = self.dir
        for f in path.split('\n'):
            current_depth = f.count('\t')
            f = f.replace('\t', '')

            if current_depth == 0:
                pass
            elif current_depth == depth + 1:
                current = current.child_folder[-1]
                depth += 1
            elif current_depth <= depth:
                while current_depth < depth:
                    current = current.parent
                    depth -= 1
            else:
                raise IndexError('parse error!')

            if '.' in f:
                current.add_file(File(f, current))
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.longest_path = current.file[0].path
            else:
                current.add_folder(Folder(f, current))




if __name__ == '__main__':
    for path in [
        '',
        'dir',
        'file.txt',
        'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext',
        'dir\n\tsubdir1\n\t\tfile1.ext\n\tsubdir2\n\tfile2.ext',
        'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
    ]:
        file_system = FileSystem(path)
        print('@  {}\n=> [length:{}] {}'.format(
            path, len(file_system.longest_path), file_system.longest_path))
