"""The utils for SQL statements generation."""


def find_named_variables(mapping):
    """Find correspondance between variable and relation and its attribute."""
    var_dictionary = dict()
    for relation_instance in mapping.lhs:
        for i, variable in enumerate(relation_instance.variables):
            name = relation_instance.relation.name
            field = relation_instance.relation.fields[i]
            if variable not in var_dictionary.keys():
                var_dictionary.update({variable: []})
                var_dictionary[variable].append((name, field))
            else:
                if (name, field) not in var_dictionary[variable]:
                    var_dictionary[variable].append((name, field))
    return var_dictionary


def format_field(relation_name, field):
    """Util for formatting relation name and field into sql syntax."""
    return "%s.%s" % (relation_name, field)


def generate_insertion_tuple(mapping):
    """For the given mapping generate insertion tuple."""
    # we need to find from mappings the dictionary
    # { variable_name: (relation_name, field) }
    named_variables = find_named_variables(mapping)
    for relation_instance in mapping.rhs:

        # generate table with its attribures
        fields = ", ".join(relation_instance.relation.fields)
        table_name = "%s(%s)" % (relation_instance.relation.name,
                                 fields)

        # generate attributes to select
        selection_attributes = []
        for i, variable in enumerate(relation_instance.variables):
            if type(variable) == str:
                selection_attributes.append(
                    format_field(named_variables[variable][0][0],
                                 named_variables[variable][0][1]))
            else:
                skolem_list = [" || %s.%s || " % (
                    named_variables[arg][0][0],
                    named_variables[arg][0][1]) for arg in variable.arguments]
                skolem_term = "\',\'".join(skolem_list)
                selection_attributes.append(
                    "\'f[%s,%s](\' %s \')\'" %
                    (variable.mapping_name,
                     format_field(relation_instance.relation.name,
                                  relation_instance.relation.fields[i]),
                     skolem_term))
        selection_attributes = ", ".join(selection_attributes)

        # generate from statement with inner joins
        join_statement = ""
        if len(mapping.lhs) > 1:
            for elem in named_variables.values():
                if len(elem) > 1:
                    join_statement = "%s " % elem[0][0]
                    for i in range(1, len(elem)):
                        join_statement += "INNER JOIN %s ON %s = %s " % (
                            elem[i][0],
                            format_field(elem[i - 1][0], elem[i - 1][1]),
                            format_field(elem[i][0], elem[i][1]))
        else:
            join_statement = "%s " % mapping.lhs[0].relation.name
        return (table_name, selection_attributes, join_statement)


def generate_sql(mappings):
    """Generate INSERT statement for the set of tgds."""
    statement_template =\
        "INSERT INTO %s\n SELECT %s \n FROM %s;\n"
    sql_statements = []
    for mapping in mappings:
        insertion_tuple = generate_insertion_tuple(mapping)
        sql = statement_template % insertion_tuple
        sql_statements.append(sql)
    return "\n".join(sql_statements)


def generate_target(target):
    sql = ""
    for relation in target:
        sql += "CREATE TABLE %s (%s);\n" % (relation.name, ", ".join([str(f) + " TEXT" for f in relation.fields]))
    return sql
