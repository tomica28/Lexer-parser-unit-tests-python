import unittest
import ut_parser
import ut_lexer
import parse_model

class ParseClassTest1(unittest.TestCase):
    def test_class(self):
        code = """\
class Generator:
    def generate(self, number_of_shares, lower_price_limit, upper_price_limit):
        sum = number_of_shares
        i = 0
        stmt = True
        while stmt is True:
            i -= 1
            if i == 0:
                print lower_price_limit
                stmt = False
            else:
                print upper_price_limit
"""

        result = ut_parser.parser.parse(code, lexer=ut_lexer.lexer)

        # class Generator
        self.assertTrue(isinstance(result, parse_model.Program))
        self.assertTrue(isinstance(result.elements[0], parse_model.ClassDef))
        self.assertEqual(str(result.elements[0].name), 'Generator')
        # def generate(self, number_of_shares, lower_price_limit, upper_price_limit):
        self.assertTrue(isinstance(result.elements[0].methods[0], parse_model.FuncDef))
        self.assertEqual(str(result.elements[0].methods[0].name), 'generate')
        self.assertEqual(str(result.elements[0].methods[0].parameters[0]), 'self')
        self.assertEqual(str(result.elements[0].methods[0].parameters[1]), 'number_of_shares')
        self.assertEqual(str(result.elements[0].methods[0].parameters[2]), 'lower_price_limit')
        self.assertEqual(str(result.elements[0].methods[0].parameters[3]), 'upper_price_limit')

        self.assertTrue(isinstance(result.elements[0].methods[0].suite, parse_model.IndentedStmtList))
        # sum = number_of_shares
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[0], parse_model.StmtList))
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[0].statement_list[0], parse_model.Assignment))
        self.assertEqual(str(result.elements[0].methods[0].suite.statement_list[0].statement_list[0].target), 'sum')
        self.assertEqual(str(result.elements[0].methods[0].suite.statement_list[0].statement_list[0].expression), 'number_of_shares')
        # i = 0
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[1], parse_model.StmtList))
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[1].statement_list[0], parse_model.Assignment))
        self.assertEqual(str(result.elements[0].methods[0].suite.statement_list[1].statement_list[0].target), 'i')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[1].statement_list[0].expression.value, '0')
        # stmt = True
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[2], parse_model.StmtList))
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[2].statement_list[0], parse_model.Assignment))
        self.assertEqual(str(result.elements[0].methods[0].suite.statement_list[2].statement_list[0].target), 'stmt')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[2].statement_list[0].expression.value, 'True')
        # while stmt is True:
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3], parse_model.WhileStmt))
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].condition, parse_model.BinaryExpression))
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].condition.op1.value, 'stmt')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].condition.operator, 'is')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].condition.op2.value, 'True')

        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].suite, parse_model.IndentedStmtList))
        # i -= 1
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[0], parse_model.StmtList))
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[0].statement_list[0], parse_model.AugmentedAssignment))
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[0].statement_list[0].target.value, 'i')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[0].statement_list[0].operator, '-=')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[0].statement_list[0].expression.value, '1')
        # if i == 0:
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1], parse_model.IfStmt))

        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][0], parse_model.BinaryExpression))
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][0].op1.value, 'i')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][0].operator, '==')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][0].op2.value, '0')
        # print lower_price_limit
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][1].statement_list[0].statement_list[0], parse_model.PrintStmt))
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][1].statement_list[0].statement_list[0].arguments[0].value, 'lower_price_limit')
        # stmt = False
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][1].statement_list[1].statement_list[0], parse_model.Assignment))
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][1].statement_list[1].statement_list[0].target.value, 'stmt')
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].blocks[0][1].statement_list[1].statement_list[0].expression.value, 'False')
        # print upper_price_limit
        self.assertTrue(isinstance(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].else_suite.statement_list[0].statement_list[0], parse_model.PrintStmt))
        self.assertEqual(result.elements[0].methods[0].suite.statement_list[3].suite.statement_list[1].else_suite.statement_list[0].statement_list[0].arguments[0].value, 'upper_price_limit')
if __name__ == '__main__':
    unittest.main()