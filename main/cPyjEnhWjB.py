import os
import json
import random
import string
class FileUtility:
    def __init__(self, directory):
        self.directory = directory
    def create_file(self, filename, content):
        with open(os.path.join(self.directory, filename), 'w') as f:
            f.write(content)
    def read_file(self, filename):
        with open(os.path.join(self.directory, filename), 'r') as f:
            return f.read()
    def delete_file(self, filename):
        os.remove(os.path.join(self.directory, filename))
    def list_files(self):
        return os.listdir(self.directory)
class RandomStringGenerator:
    @staticmethod
    def generate(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
def main():
    utility = FileUtility('./')
    utility.create_file('test.txt', 'Hello, World!')
    print(utility.read_file('test.txt'))
    print(utility.list_files())
    utility.delete_file('test.txt')
    print(utility.list_files())
    random_string = RandomStringGenerator.generate(10)
    utility.create_file('random.txt', random_string)
    print(utility.read_file('random.txt'))
    utility.delete_file('random.txt')
if __name__ == '__main__':
    main()
