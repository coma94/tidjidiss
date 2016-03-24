import fileinput

from input_parser import parse
from input_parser import source, target, tgds
from skolemizer import skolemize
from sql_generator import generate_sql


if __name__ == '__main__':
    # Reads the input file from stdin
    input_file = ""
    for line in fileinput.input():
        input_file += line

    # Parse input, skolemize & generates sql
    parse(input_file)
    skolemized_tgds = skolemize(tgds)
    sql = generate_sql(skolemized_tgds)

    # output final sql
    print(sql)
    
