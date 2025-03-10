import ply.lex as lex

tokens = (
    'QUESTION', 'COLON', 'IDENTIFIER', 'NUMBER','EQUALS','RELOP','LPAREN','RPAREN', 'SEMICOLON'
)

t_QUESTION = r'\?'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_EQUALS=r'\='
t_RELOP=r'==|!=|>=|<=|>|<'
t_COLON = r':'
t_SEMICOLON = r';'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'[0-9]+'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    data=input("Enter the code:")
    if(data==''):
        data = "y = (2>30) ? 2 : 30 ;"
    lexer.input(data)
    for tok in lexer:
        print(tok)
#if the user enters an empty string, it will take the default value mentioned in the data to handle the construct
''' This code recognizes tokens such as
    'QUESTION'-?, 
    'COLON'-:, 
    'IDENTIFIER'-variable name, 
    'NUMBER'-0,123,etc,
    'EQUALS'-=,
    'RELOP'-==,!=,>=,<=,>,<,
    'LPAREN'-(,
    'RPAREN'-), 
    'SEMICOLON'-;
    Input:
User provides a string containing code.
If no input is provided, a default example (y = (2>30) ? 2 : 30;) is used.
'''