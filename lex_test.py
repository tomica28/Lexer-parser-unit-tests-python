import unittest
import ut_lexer


class IndentTest(unittest.TestCase):
    def testIndent(self):
        code_to_test = '''\
code
    code
    code
        code
    code
code\
        '''
        expected_tokens = ['INDENT', 'INDENT', 'DEDENT', 'DEDENT']
        ut_lexer.lexer.input(code_to_test)
        tokens = [tok.type for tok in ut_lexer.lexer if tok.type == 'INDENT' or tok.type == 'DEDENT']
        self.assertListEqual(tokens, expected_tokens, 'Wrong indenting sequence!')


class LiteralTest(unittest.TestCase):
    def testStringLiteral(self):
        code = '"some_text" "x"abc"y"'
        expected_tokens = ['"some_text"', '"x"', '"y"']
        ut_lexer.lexer.input(code)
        tokens = [tok.value for tok in ut_lexer.lexer if tok.type == 'STRING_LITERAL']
        self.assertListEqual(tokens, expected_tokens,
                             'Wrong token list! ' + str(tokens) + ' expected: ' + str(expected_tokens))

    def testIntegerLiteral(self):
        code_to_test = '0 123 19940'
        expected_tokens = ['0', '123', '19940']
        ut_lexer.lexer.input(code_to_test)
        tokens = [tok.value for tok in ut_lexer.lexer if tok.type == 'INTEGER_LITERAL']
        self.assertListEqual(tokens, expected_tokens,
                             'Wrong token list! ' + str(tokens) + ' expected: ' + str(expected_tokens))

    def testFloatingPointLiteral(self):
        # given
        code_to_test = '.1 1.1 1. 2e10 2e-10 1.e01 1.1e1'
        expected_tokens = code_to_test.split()
        # when
        ut_lexer.lexer.input(code_to_test)
        tokens = [tok.value for tok in ut_lexer.lexer if tok.type == 'FLOATING_POINT_LITERAL']
        # then
        self.assertListEqual(tokens, expected_tokens,
                             'Wrong token list! ' + str(tokens) + ' expected: ' + str(expected_tokens))


if __name__ == '__main__':
    unittest.main()