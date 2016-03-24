from sys import argv, stdin
import sqlite3

from input_parser import parse
from input_parser import target, tgds
from skolemizer import skolemize
from sql_generator import generate_sql, generate_target


if __name__ == '__main__':
    # Reads the input file from stdin
    input_file = ""
    for line in stdin:
        input_file += line

    # Parse input, skolemize & generates sql
    parse(input_file)
    skolemized_tgds = skolemize(tgds)
    sql = generate_sql(skolemized_tgds)

    # Is it integrated with sqlite ?
    if len(argv) > 1 and argv[1] == "-sqlite3":
        database = argv[2]

        target_sql = generate_target(target)

        print("/* Executing the following code on", database, "... */")
        print(target_sql)
        print(sql)
        
        conn = sqlite3.connect(database)
        c = conn.cursor()

        for line in target_sql.split(';'):
            c.execute(line)
        for line in sql.split(';'):
            c.execute(line)
        conn.commit()
        conn.close()
        print()
        print("/* Done !*/")
        
        
    else:
        # output final sql
        print(sql)
    
