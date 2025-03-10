import ply.yacc as yacc
from lexer_declare_assign import tokens

def p_program(p):
    '''program : statement_list'''
    print("Parsing complete!")

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''

def p_statement(p):
    '''statement : var_declaration
                 | assignment'''

def p_var_declaration(p):
    '''var_declaration : TYPE IDENTIFIER EQUALS expression SEMICOLON'''
    print(f"Declared variable '{p[2]}' of type '{p[1]}' with initial value '{p[4]}'")

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression SEMICOLON'''
    print(f"Assigned '{p[1]}' to '{p[3]}'")

def p_expression(p):
    '''expression : INT_NUMBER
                  | FLOAT_NUMBER
                  | IDENTIFIER
                  | BOOLEAN_VALUE
                  | CHARACTER
                  | STRING'''
    p[0] = p[1] if len(p) == 2 else None 

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
if __name__ == "__main__":
   data=input("Enter the code:")
   if(data==''):
    data='''
    String a = "abc";
    int y = 20;
    float x = 10.00;
    char letter = 'A';
    boolean isTrue = true;
    '''
parser.parse(data)
#if the user enters an empty string, it will take the default value mentioned in the data to handle the construct
'''Parses Java-style constructs for:
Variable declarations: Ensures correct structure with type, identifier, assignment, and terminator.
Assignments: Validates assignment statements.
Detects and reports syntax errors, including:
    Unexpected tokens.
    Missing or misplaced components.
Supports multiple statement parsing.
Error Handling: Reports syntax errors with details of the unexpected token or EOF (end-of-file).
Example: Input int x = ; generates: Syntax error at ';'.
Default Code Block: If no input is provided, the parser processes a predefined Java-like code block for testing.
'''