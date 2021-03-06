# ------------------------------------------------------------
# Lexer para C#
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'operators',
   'logicOperators',
   'relationalOperators',
   'LPAREN',
   'RPAREN',
   'keyword',
   'identificador',
   'inicioBloque',
   'finBloque',
   'finInstruccion',
   'asignacion',
   'comentario',
   'comentario_bloque',
   'cadena',
   'coma',
   'punto'
)

# Regular expression rules for simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_inicioBloque = r'\{'
t_finBloque = r'\}'
t_finInstruccion = r'\;'
t_asignacion = r'\='
t_coma= r'\,'
t_punto=r'\.'

# A regular expression rule with some action code
def t_comentario(t):
    r'\/\/.*'
    return t

def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    return t

def t_relationalOperators(t):
  r'(\==)|(\<)|(\>)|(\!=)|(\>=)|(\<=)'
  return t

def t_operators(t):
  r'(\+)|(\-)|(\*)|(\/)|(\%)|(\==)|(\+{2})|(\-{2})'
  return t

def t_logicOperators(t):
  r'(\|{2})|(\&{2})|(\!)'
  return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_keyword(t):
    r'(int)|(float)|(char)|(return)|(if)|(else)|(do)|(while)|(for)|(void)|(using)|(WriteLine)|(enum)|(true)|(switch)|(try)|(catch)|(this)'
    return t

def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

def t_cadena(t):
    r'\".*\"'
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)    
    return t

# Build the lexer
lexer = lex.lex()

def miLexer():
    f = open('fuente.cs','r')
    lexer.input(f.read())
    while True:
        tok=lexer.token()
        if not tok:
            break
        #print(tok)
        if tok.type != 'comentario' and tok.type != 'comentario_bloque':
          print(' type: ',tok.type,'\n',
            'Value: ',tok.value,'\n',
              'line #: ',tok.lineno,'\n',
              'character #: ',tok.lexpos)
          print('---------------')


if __name__ == "__main__":
  miLexer()
        
        
        