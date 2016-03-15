"""."""
import ply.yacc as yacc
from lexer import tokens

from data_structures import Schema, Relation, RelationInstance, Mapping


source = Schema()
target = Schema()
tgds = list()


def p_start(p):
    'start : SOURCE schema_source TARGET schema_target MAPPING tgds'
    p[0] = (p[2], p[4], p[6])

def p_schema_source(p):
    '''schema_source : relation schema_source
                     | relation'''
    source.append(p[1])
    p[0] = source

def p_schema_target(p):
    '''schema_target : relation schema_target
                     | relation'''
    target.append(p[1])
    p[0] = target

def p_relation(p):
    'relation : NAME P_OPEN atts P_CLOSE'
    rel = Relation(p[1], p[3][::-1])
    p[0] = rel

def p_atts(p):
    '''atts : NAME COMMA atts
            | NAME'''
    p[0] = []
    if len(p) == 4:
        p[0] = p[3]
    p[0].append(p[1])

def p_tgds(p):
    '''tgds : tgd tgds
         | tgd'''
    tgds.append(p[1])
    p[0] = tgds

#left/tight to know where to search the relations
def p_tgd(p):
    'tgd : left_query ARROW right_query FULLSTOP'
    tgd = Mapping(p[1][::-1], p[3][::-1])
    p[0] = tgd

def p_left_query(p):
    '''left_query : left_atom COMMA left_query
                  | left_atom'''
    p[0] = []
    if len(p) == 4:
        p[0] = p[3]
    p[0].append(p[1])

def p_right_query(p):
    '''right_query : right_atom COMMA right_query
                   | right_atom'''
    p[0] = []
    if len(p) == 4:
        p[0] = p[3]
    p[0].append(p[1])

# Left atom of tgds. Search the relations in the source schema.
def p_left_atom(p):
    'left_atom : NAME P_OPEN args P_CLOSE'
    found = False
    for rel in source:
        if rel.name == p[1]:
            found = True
            p[0] = RelationInstance(rel, p[3][::-1])
            break
    
    if not found:
        print("ERROR: no relation named", p[1], "in source")

#Right atom of tgds. Search the relations in the target schema.
def p_right_atom(p):
    'right_atom : NAME P_OPEN args P_CLOSE'
    found = False
    for rel in target:
        if rel.name == p[1]:
            found = True
            p[0] = RelationInstance(rel, p[3][::-1])
            break
    
    if not found:
        print("ERROR: no relation named", p[1], "in target")

def p_args(p):
    '''args : value COMMA args
         | value'''
    p[0] = []
    if len(p) == 4:
        p[0] = p[3]
    p[0].append(p[1])

def p_value(p):
    '''value : VARIABLE
             | CONSTANT'''
    if p[1][0] == '$':
        p[0] = p[1]
    else:
        p[0] = int(p[1])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

def parse(data):
    parser.parse(data)
    source.reverse()
    target.reverse()
    tgds.reverse()

if __name__ == '__main__':
    file = "examples/example-input-file.txt"
    with open(file, 'r+') as f:
        data = f.read()
        parser.parse(data)
