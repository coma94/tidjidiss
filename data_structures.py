"""."""


class Schema(list):
    # relations = [Relation1, Relation2, ..]
    def __init__(self, *args):
        list.__init__(self, *args)


class Relation:
    # name
    # fields = [Field1, Field2, ...]
    def __init__(self, name, attributes):
        self.name = name
        self.fields = attributes


class RelationInstance:
    # relation = Relation()
    # variables = [VarName1, VarName2, ..] position is important!!!
    def __init__(self, relation, variables):
        self.relation = relation
        self.variables = variables


class Mapping:
    # rhs - right hand side of rule
    # lhs - left hand side of rule
    # rhs = [RelationInstance1, RelationInstance2, ...] - conjunction of these
    # relations
    # lhs = same
    def __init__(self, rhs, lhs):
        self.rhs = rhs
        self.lhs = lhs


class SkolemTerm:
    # mapping_name = ..
    # variable = ..
    # arguments = [VarName1, Varname2, ..]
    pass


class SkolemizedMapping(Mapping):
    # it can contain in rhs and lhs both variables and SkolemTerms
    pass
