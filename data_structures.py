"""."""


class Schema:
    # relations = [Relation1, Relation2, ..]
    pass


class Relation:
    # name
    # fields = [Field1, Field2, ...]
    pass


class RelationInstance:
    # relation = Relation()
    # variables = [VarName1, VarName2, ..] position is important!!!
    pass


class Mapping:
    # rhs - right hand side of rule
    # lhs - left hand side of rule
    # rhs = [RelationInstance1, RelationInstance2, ...] - conjunction of these
    # relations
    # lhs = same
    pass


class SkolemTerm:
    # mapping_name = ..
    # variable = ..
    # arguments = [VarName1, Varname2, ..]
    pass


class SkolemizedMapping(Mapping):
    # it can contain in rhs and lhs both variables and SkolemTerms
    pass
