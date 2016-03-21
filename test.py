"""Test implemeted scripts."""
from input_parser import parse
# from parser import source
# from parser import target
from input_parser import tgds
from skolemizer import skolemize
from sql_generator import generate_sql


if __name__ == '__main__':
    file = "examples/example-input-file.txt"
    with open(file, 'r+') as f:
        data = f.read()
        parse(data)
        skolemized_tgds = skolemize(tgds)
        for i, sk_tgd in enumerate(skolemized_tgds):
            print("m%d:" % (i + 1))
            print("Left hand side: ")
            for instance in sk_tgd.lhs:
                print(instance.relation.name)
                print(instance.variables)
            print("Right hand side:")
            for instance in sk_tgd.rhs:
                print(instance.relation.name)
                for var in instance.variables:
                    if type(var) == str:
                        print(var)
                    else:
                        print("f_%s,%s(%s)" % (
                            var.mapping_name,
                            var.variable,
                            ",".join(var.arguments)))
            print("\n")
        sql = generate_sql(skolemized_tgds)
        print(sql)
