"""
comp805
homework1

Lloyd Dagoc
University of New Hanmpshire
"""

from dns import resolver
import subprocess


class homework1():

    def executeSampleMethod():
        my_resolver = resolver.Resolver()
        line_list = []

        try:
            with open("dig-urls.txt") as f_handler:
                for line_in_file in f_handler:
                    line_in_file = line_in_file.rstrip()

                    print(line_in_file)
                    dig_info = my_resolver.query(line_in_file, "A")

                    # create dictionary of lists
                    # dig_container = [i for i in dig_info]
                    for data in dig_info:
                        print(data)

        except IOError:
            print("File does not exist")

    if __name__ == '__main__':
        executeSampleMethod()
