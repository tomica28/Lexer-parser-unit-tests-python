import ply.yacc as yacc
import ut_lexer
import parse_model

start = 'program'

tokens = ut_lexer.Lexer.tokens

def p_program(p):
    """program : NEWLINE
               | classdef
               | import_stmt
               | program NEWLINE
               | program classdef
               | program import_stmt"""
    if len(p) == 2 and p[1] != '\n':
        p[0] = parse_model.Program(p[1])
    elif len(p) == 2:
        p[0] = parse_model.Program()
    elif len(p) == 3 and p[2] != '\n':
        p[0] = parse_model.Program(program=p[1], elem=p[2])
    else:
        p[0] = parse_model.Program(program=p[1])


def p_literal(p):
    """literal : STRING_LITERAL
               | INTEGER_LITERAL
               | FLOATING_POINT_LITERAL"""
    p[0] = parse_model.Literal(p[1])


def p_identifier(p):
    """identifier : IDENTIFIER"""
    p[0] = parse_model.Identifier(p[1])


def p_atom(p):
    """atom : identifier
            | literal"""
    p[0] = p[1]

def p_primary(p):
    """primary : atom
               | attributeref
               | call"""
    p[0] = p[1]


def p_attributeref(p):
    """attributeref : primary DOT identifier"""
    p[0] = parse_model.AttributeRef(p[1], p[3])


def p_call(p):
    """call : primary OPEN_PARENTHESIS CLOSE_PARENTHESIS
            | primary OPEN_PARENTHESIS positional_arguments CLOSE_PARENTHESIS"""
    if len(p) == 4:
        p[0] = parse_model.Call(p[1], [])
    else:
        p[0] = parse_model.Call(p[1], p[3])


def p_positional_arguments(p):
    """positional_arguments : expression
                            | positional_arguments COMA expression"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_u_expr(p):
    """u_expr : primary
              | MINUS primary
              | PLUS primary"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = parse_model.UnaryExpression(value=p[2], operator=p[1])


def p_m_expr(p):
    """m_expr : u_expr
              | m_expr ASTERISK u_expr
              | m_expr SLASH u_expr
              | m_expr PERCENT u_expr"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = parse_model.BinaryExpression(p[1], p[2], p[3])


def p_a_expr(p):
    """a_expr : m_expr
              | a_expr PLUS m_expr
              | a_expr MINUS m_expr"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = parse_model.BinaryExpression(p[1], p[2], p[3])


def p_cmp_operator(p):
    """cmp_operator : LT
                    | GT
                    | EQ
                    | GTE
                    | LTE
                    | NE
                    | IS
                    | IS NOT"""
    if len(p) == 3:
        p[1] = p[1] + " " + p[2]
    p[0] = p[1]


def p_comparison(p):
    """comparison : a_expr
                  | a_expr cmp_operator a_expr"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = parse_model.BinaryExpression(p[1], p[2], p[3])


def p_or_test(p):
    """or_test : and_test
               | or_test OR and_test"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = parse_model.BinaryExpression(p[1], p[2], p[3])


def p_and_test(p):
    """and_test : not_test
                | and_test AND not_test"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = parse_model.BinaryExpression(p[1], p[2], p[3])


def p_not_test(p):
    """not_test : comparison
                | NOT not_test"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = parse_model.UnaryExpression(operator=p[1], value=p[2])


def p_expression(p):
    """expression : or_test
                  | or_test IF or_test ELSE expression"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = parse_model.ConditionalExpression(p[1], p[3], p[5])


def p_simple_stmt(p):
    """simple_stmt : expression
                   | assignment_stmt
                   | augmented_assignment_stmt
                   | pass_stmt
                   | print_stmt
                   | return_stmt
                   | continue_stmt
                   | break_stmt"""
    p[0] = p[1]


def p_assignment_stmt(p):
    """assignment_stmt : identifier ASSIGNMENT expression
                       | attributeref ASSIGNMENT expression"""
    p[0] = parse_model.Assignment(p[1], p[3])

def p_augop(p):
    """augop : PLUS_ASSIGNMENT
             | MINUS_ASSIGNMENT
             | ASTERISK_ASSIGNMENT
             | SLASH_ASSIGNMENT
             | PERCENT_ASSIGNMENT"""
    p[0] = p[1]

def p_augmented_assignment_stmt(p):
    """augmented_assignment_stmt : identifier augop expression
                                 | attributeref augop expression"""
    p[0] = parse_model.AugmentedAssignment(p[1], p[2], p[3])

def p_pass_stmt(p):
    """pass_stmt : PASS"""
    p[0] = parse_model.PassStmt()

def p_print_stmt(p):
    """print_stmt : PRINT positional_arguments"""
    p[0] = parse_model.PrintStmt(p[2])

def p_return_stmt(p):
    """return_stmt : RETURN expression
                   | RETURN"""
    if len(p) == 2:
        p[0] = parse_model.ReturnStmt(parse_model.Identifier('None'))
    else:
        p[0] = parse_model.ReturnStmt(p[2])

def p_continue_stmt(p):
    """continue_stmt : CONTINUE"""
    p[0] = parse_model.ContinueStmt()

def p_break_stmt(p):
    """break_stmt : BREAK"""
    p[0] = parse_model.BreakStmt()

def p_import_stmt(p):
    """import_stmt : IMPORT module"""
    p[0] = parse_model.ImportStmt(p[2])

def p_module(p):
    """module : identifier
              | module DOT identifier"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = str(p[1]) + '.' + str(p[3])



def p_compound_stmt(p):
    """compound_stmt : expression
                     | while_stmt
                     | if_stmt"""
    p[0] = p[1]

def p_suite(p):
    """suite : stmt_list NEWLINE
             | NEWLINE INDENT indented_stmt_list DEDENT"""
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = p[3]

def p_statement(p):
    """statement : stmt_list NEWLINE
                 | compound_stmt"""
    p[0] = p[1]

def p_indented_stmt_list(p):
    """indented_stmt_list : statement
                          | indented_stmt_list statement"""
    if len(p) == 2:
        p[0] = parse_model.IndentedStmtList(p[1])
    else:
        p[1].add_stmt(p[2])
        p[0] = p[1]

def p_stmt_list(p):
    """stmt_list : simple_stmt
                 | stmt_list SEMICOLON simple_stmt"""
    if len(p) == 2 or len(p) == 3:
        p[0] = parse_model.StmtList(p[1])
    else:
        p[1].add_stmt(p[3])
        p[0] = p[1]

def p_while_stmt(p):
    """while_stmt : WHILE expression COLON suite
                  | WHILE expression COLON suite ELSE COLON suite"""
    if len(p) == 5:
        p[0] = parse_model.WhileStmt(p[2], p[4], None)
    else:
        p[0] = parse_model.WhileStmt(p[2], p[4], p[7])

def p_if_stmt(p):
    """if_stmt : IF expression COLON suite
               | IF expression COLON suite ELSE COLON suite
               | IF expression COLON suite elifs
               | IF expression COLON suite elifs ELSE COLON suite"""
    if len(p) == 5:
        p[0] = parse_model.IfStmt([(p[2], p[4])])
    elif len(p) == 6:
        p[0] = parse_model.IfStmt([(p[2], p[4])]+p[5])
    elif len(p) == 8:
        p[0] = parse_model.IfStmt([(p[2], p[4])], p[7])
    elif len(p) == 9:
        p[0] = parse_model.IfStmt([(p[2], p[4])] + p[5], p[8])


def p_elifs(p):
    """elifs : ELIF expression COLON suite
             | elifs ELIF expression COLON suite"""
    if len(p) == 5:
        p[0] = [(p[2], p[4])]
    else:
        p[0] = p[1] + [(p[3], p[5])]

def p_funcdef(p):
    """funcdef : DEF identifier OPEN_PARENTHESIS CLOSE_PARENTHESIS COLON suite
               | DEF identifier OPEN_PARENTHESIS parameter_list CLOSE_PARENTHESIS COLON suite"""
    if len(p) == 7:
        p[0] = parse_model.FuncDef(p[2], [], p[6])
    else:
        p[0] = parse_model.FuncDef(p[2], p[4], p[7])

def p_parameter_list(p):
    """parameter_list : identifier
                      | parameter_list COMA identifier"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_classdef(p):
    """classdef : CLASS identifier COLON pass_stmt
                | CLASS identifier COLON NEWLINE INDENT class_suite DEDENT
                | CLASS identifier OPEN_PARENTHESIS identifier CLOSE_PARENTHESIS COLON pass_stmt
                | CLASS identifier OPEN_PARENTHESIS identifier CLOSE_PARENTHESIS COLON NEWLINE INDENT class_suite DEDENT"""
    if len(p) == 5:
        p[0] = parse_model.ClassDef(p[2], None, p[4])
    if len(p) == 8 and p[7].__class__ is not parse_model.PassStmt:
        p[0] = parse_model.ClassDef(p[2], None, p[6])
    elif len(p) == 8:
        p[0] = parse_model.ClassDef(p[2], p[4], p[7])
    elif len(p) == 11:
        p[0] = parse_model.ClassDef(p[2], p[4], p[9])

def p_class_suite(p):
    """class_suite : funcdef
                   | class_suite funcdef"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_error(p):
    if p:
        print("Syntax error at token {} in line {}".format(p.type, p.lineno))
        #discard the token
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def generate_program(source):
    file = open(source)
    return parser.parse(file.read(), lexer=ut_lexer.lexer)






