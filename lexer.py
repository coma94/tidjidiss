"""The utils for parsing the input files."""
import ply.lex as lex


tokens = [
    "SOURCE",
    "TARGET",
    "MAPPING",
    "P_OPEN",
    "P_CLOSE",
    "COMMA",
    "ARROW",
    "FULLSTOP",
    "NAME",
    "VARIABLE",
    "CONSTANT",
]


t_SOURCE = r"SOURCE"
t_TARGET = r"TARGET"
t_MAPPING = r"MAPPING"
t_P_OPEN = r"\("
t_P_CLOSE = r"\)"
t_COMMA = r","
t_ARROW = r"->"
t_FULLSTOP = r"\."
t_VARIABLE = r"\$[a-zA-Z_]+[a-zA-Z\d_]*"
t_CONSTANT = r"\d+"

t_ignore = " \n\t"


def t_NAME(t):
    r"[a-zA-Z_]+[a-zA-Z\d_]*"
    if t.value == "SOURCE":
        t.type = "SOURCE"
    if t.value == "TARGET":
        t.type = "TARGET"
    if t.value == "MAPPING":
        t.type = "MAPPING"
    return t


def t_error(t):
    """."""
    raise TypeError("Unknown text '%s'" % (t.value,))


def parse(file):
    """."""
    with open(file, 'r+') as f:
        data = f.read()
        lex.lex()
        lex.input(data)
        for tok in iter(lex.token, None):
            print(repr(tok.type), repr(tok.value))

if __name__ == '__main__':
    parse("examples/example-input-file.txt")
