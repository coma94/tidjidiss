"""Definition all data types needed for our schema mapping purposes."""


class Schema(list):
    """Datastructure of shema definition."""

    def __init__(self, *args):
        """Input: list of instances of relation [Rel1, Rel2, ..]."""
        list.__init__(self, *args)


class Relation:
    """Datastructure of relation."""

    def __init__(self, name, attributes):
        """Input name of relation and fields (attributes)."""
        self.name = name
        self.fields = attributes


class RelationInstance:
    """Datastructure of relation instance (used in mappings)."""

    def __init__(self, relation, variables):
        """Initialize the relation instance.

        Input arguments
        - relation instance of Relation()
        - list of variables [VarName1, VarName2, ..]
        and their position is important
        """
        self.relation = relation
        self.variables = variables


class Mapping:
    """Datastructure of mapping."""

    def __init__(self, lhs, rhs):
        """Initialize the mapping.

        rhs - right hand side of rule
        lhs - left hand side of rule, where
        both lhs and rhs are lists of RelationInstance() objects.
        We interpret the list as conjunction of these relations.
        """
        self.lhs = lhs
        self.rhs = rhs


class SkolemTerm:
    """Datastructure of skolem term."""

    def __init__(self, name, variable, arguments):
        """Initialize skolem term.

        Takes on input mapping_name, variable that is skolemized
        arguments = [VarName1, Varname2, ..] list of variables
        on which skolem term depends
        """
        self.mapping_name = name
        self.variable = variable
        self.arguments = arguments


class SkolemizedMapping(Mapping):
    """Datastructure of skolemized mapping."""

    def __init__(self, lhs, rhs):
        """The same as mapping but can contain as variables skolm terms."""
        self.lhs = lhs
        self.rhs = rhs
