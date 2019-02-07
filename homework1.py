"""
comp835
homework1 - a class implementation to illustrate using a dns
resolver python package that reads through a file containing
hostnames

Python version: 3.6.6
Required PIP Packages: homework1_requirements.txt

Lloyd Dagoc
University of New Hampshire
"""

from dns import resolver
import subprocess
import sys


class Homework1():

    def __init__(self, passed_args):
        self.passed_args = passed_args

    def query_filelist(self):
        for i in passed_args:
            self.resolve_hosts(i)

    def resolve_hosts(self, filename):
        filename = filename
        my_resolver = resolver.Resolver()

        try:
            with open(filename) as f_handler:

                dig_dict = {}
                for line_in_file in f_handler:
                    line_in_file = line_in_file.rstrip()
                    dig_info = my_resolver.query(line_in_file, "A")

                    dig_list = []
                    for data in dig_info:
                        dig_list.append(data)

                    dig_dict[line_in_file] = dig_list
                print(dig_dict)

        except IOError:
            print(filename + ": File does not exist")


if __name__ == '__main__':
    passed_args = sys.argv[1:]
    if len(passed_args) <= 0:
        print("Specify a filename input")
        sys.exit
    else:
        homework_obj = Homework1(passed_args)
        homework_obj.query_filelist()
