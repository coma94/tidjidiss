"""The utils for skolemization of tgds."""

from data_structures import SkolemizedMapping
from data_structures import SkolemTerm
from data_structures import RelationInstance


def skolemize(mappings):
    """Take list of mappings and return the list of scholemized mappings."""
    scholemized_mappings = []

    for i, mapping in enumerate(mappings):
        skol_lhs = mapping.lhs
        skol_rhs = []
        universal_variables = []
        for instance in mapping.lhs:
            new_variables =\
                [var for var in instance.variables
                    if var not in universal_variables]
            universal_variables.extend(new_variables)
        for instance in mapping.rhs:
            skol_variables = []
            for var in instance.variables:
                if var not in universal_variables:
                    # TODO: now we make skolem term depend on all universal
                    # variables but later change to depend only ones from rhs
                    # ORDER OF ARGUMENTS IS NOT PRESERVED
                    skol_term = SkolemTerm(
                        "m%d" % (i + 1), var, universal_variables)
                    skol_variables.append(skol_term)
                else:
                    skol_variables.append(var)
            skol_rhs.append(
                RelationInstance(instance.relation, skol_variables))
        scholemized_mappings.append(SkolemizedMapping(skol_lhs, skol_rhs))
    return scholemized_mappings
