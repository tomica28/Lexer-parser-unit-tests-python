import ut_parser
import parse_model

class unittest_generator:

    def test_generate(self, code_file_name, tests_file_name):
        with open(code_file_name) as code_file:
            result = ut_parser.generate_program(code_file_name)
            if(result == None):
                raise Exception('File should only contain class definitions')
            elif(len(result.elements) == 0):
                raise Exception('File is empty.')
            tests_file = open(tests_file_name, "w+")
            tests_file.write('import unittest\n\n')
            for class_instance in result.elements:
                if(isinstance(class_instance, parse_model.ClassDef) == False):
                    continue
                for method_instance in class_instance.methods:
                    if(str(method_instance.name) == '__init__'):
                        continue
                    tests_file.write('class test_class_' + str(class_instance.name) + '_method_' + str(method_instance.name) + '(unittest.TestCase):\n' )
                    tests_file.write('\tdef test_1(self):\n\t\tself.fail(\'Not yet implemented\')\n')
                    if(len(method_instance.parameters) > 1):
                        tests_file.write('\tdef test_parameters_1(self, ')
                        for parameter in method_instance.parameters:
                            if(method_instance.parameters.index(parameter) == (len(method_instance.parameters) - 1)):
                                tests_file.write(str(parameter) + '):\n\t\tself.fail(\'Not yet implemented\')\n')
                            elif(str(parameter) == 'self'):
                                continue
                            else:
                                tests_file.write(str(parameter) + ', ')
                tests_file.write('\n')

