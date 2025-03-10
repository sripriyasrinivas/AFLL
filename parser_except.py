import ply.yacc as yacc
from lexer_except import tokens
precedence = (
    ('left', 'DIVIDE'),
    ('right', 'EQUAL'),
)

def p_program(p):
    '''program : try_catch_block'''
    p[0] = p[1]

def p_try_catch_block(p):
    '''try_catch_block : TRY LBRACE statement_list RBRACE CATCH LPAREN EXCEPTION IDENTIFIER RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('try-catch', p[3], p[8], p[11])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : IDENTIFIER EQUAL expression SEMICOLON'''
    p[0] = ('assign', p[1], p[3])

def p_expression(p):
    '''expression : NUMBER
                  | IDENTIFIER
                  | expression DIVIDE expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('divide', p[1], p[3])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

if __name__ == "__main__":
    data=input("Enter the code:")
    if(data==''):
        data = '''try {
            a = 5 / 0;
        } catch (Exception e) {
            a = 0;
        }'''
    result = parser.parse(data)
    print(result)
#if the user enters an empty string, it will take the default value mentioned in the data to handle the construct
'''Input: The user provides a Java-style try-catch block. If no input is given, a default example is used.
Parsing: The input is tokenized by the lexer. The parser builds a syntax tree based on the defined grammar rules.
Output: A structured representation of the try-catch block as tuples and lists.
'''