import ply.yacc as yacc
from lexer_ternary import tokens

# Precedence rules for operators
precedence = (
    ('left', 'QUESTION', 'COLON'),  # Ternary operator
    ('left', 'RELOP'),              # Relational operators
    ('right', 'EQUALS'),            # Assignment operator (right-associative)
)

# Grammar rules
def p_program(p):
    '''program : statement
               | program statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assignment SEMICOLON'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression'''
    p[0] = ('assign', p[1], p[3])

def p_expression_ternary(p):
    '''expression : expression QUESTION expression COLON expression'''
    p[0] = ('ternary', p[1], p[3], p[5])

def p_expression_comparison(p):
    '''expression : expression RELOP expression'''
    p[0] = ('comparison', p[1], p[2], p[3])

def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER '''
    p[0] = int(p[1])

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

if __name__ == "__main__":
    data=input("Enter the code:")
    if(data==''):
        data = "y = (2>30) ? 2 : 30 ;"
    result = parser.parse(data)
    print(result)
#if the user enters an empty string, it will take the default value mentioned in the data to handle the construct
'''
To resolve ambiguities in parsing, operator precedence is defined:

Ternary Operator (? :): Lowest precedence (left-associative).
Relational Operators (==, !=, <, >, <=, >=): Higher precedence than ternary.
Assignment Operator (=): Highest precedence (right-associative).

Input:
User provides code as input.
If no input is given, a default example (y = (2 > 30) ? 2 : 30;) is used.

Parsing:
The parser validates the syntax and builds a parse tree

Output:
A nested Python tuple representing the parse tree'''