import unittest_generator
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="File with python code.")
    parser.add_argument('-o', '--output', help="Name of file with unit tests.", default= 'out.py')

    args = parser.parse_args()
    generator = unittest_generator.unittest_generator
    try:
        generator.test_generate(generator, args.input, args.output)
    except Exception as e:
        print("Type of error: {}".format(type(e)))
        print("Expection arguments: {}".format(e.args))
        print("Expection: {}".format(e))
if __name__ == '__main__':
    main()