import ply.lex as lex

tokens = (
    'TRY', 'CATCH', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'SEMICOLON', 
    'LPAREN', 'RPAREN', 'NUMBER', 'DIVIDE', 'EQUAL','EXCEPTION')

reserved = {
    'try': 'TRY',
    'catch': 'CATCH',
    'Exception':'EXCEPTION'
}

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_NUMBER = r'[0-9]+' 
t_DIVIDE = r'/' 
t_EQUAL = r'='

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER') 
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    data=input("Enter the code:")
    if(data==''):
        data = '''try {
            a=5/0;
        } catch (Exception e) {
            a=0;
        }'''
    lexer.input(data)
    for tok in lexer:
        print(tok)
#if the user enters an empty string, it will take the default value mentioned in the data to handle the construct
'''This code recognizes the tokens
    'TRY'-Try block keyword, 
    'CATCH'-Catch block keyword, 
    'IDENTIFIER'-variable name, 
    'LBRACE'-(, 
    'RBRACE'-), 
    'SEMICOLON'-;, 
    'LPAREN'-{,
    'RPAREN'-}, 
    'NUMBER'-0,123 etc, 
    'DIVIDE'-/, 
    'EQUAL'-=,
    'EXCEPTION'-Exception keyword
Handles and skips whitespaces and newline characters.
Detects and reports illegal characters with their position.
'''