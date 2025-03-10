import ply.lex as lex

tokens = (
    'TYPE', 'IDENTIFIER', 'INT_NUMBER', 'FLOAT_NUMBER',
    'CHARACTER', 'BOOLEAN_VALUE','STRING', 'EQUALS', 'SEMICOLON', 
)

reserved = {
    'int': 'TYPE',
    'float': 'TYPE',
    'char': 'TYPE',
    'boolean': 'TYPE',
    'String': 'TYPE',
}

t_EQUALS = r'='
t_SEMICOLON = r';'

def t_BOOLEAN_VALUE(t):
    r'\b(true|false)\b'
    t.value = True if t.value == 'true' else False
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER') 
    return t

def t_FLOAT_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHARACTER(t):
    r'\'(\\?.)\''
    t.value = t.value[1]
    return t

def t_STRING(t):
    r'\".*?\"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

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
   lexer.input(data)
   for token in lexer:
    print(token)
#if the user enters an empty string, it will take the default value mentioned in the data to handle the construct
'''this code recognizes tokens like  
    'TYPE'-datatype, 
    'IDENTIFIER'-variable name, 
    'INT_NUMBER'-number of int data type, 
    'FLOAT_NUMBER'-number of float data type,
    'CHARACTER'-character enclosed by '' quotes, 
    'BOOLEAN_VALUE'-true or false,
    'STRING'-string of characters enclosed by "" quotes, 
    'EQUALS' - assignment operator, 
    'SEMICOLON'-terminator
    Illegal characters are reported and skipped without halting the program.
    Line numbers are updated for multiline inputs. 
    Default Input Handling-If the user provides an empty input, predefined Java code is tokenized.
'''