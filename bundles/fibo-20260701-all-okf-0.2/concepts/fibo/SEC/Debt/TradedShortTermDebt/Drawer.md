---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: drawer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that requires a drawee to pay either a third party or themselves with respect to a bill of exchange
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N512375935eba428e8bb061de76f5a9eb
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Obligee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligee
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/Drawer
sources:
- id: fibo-source-5edf240c05
  resource: references/fibo/SEC/Debt/TradedShortTermDebt.rdf
  sha256: 5edf240c05ec5ae1a2890d6bacd728412073d70868c0908cad8aaea54d9d21bf
  title: FIBO source SEC/Debt/TradedShortTermDebt.rdf
title: drawer
type: Ontology Class
---

# drawer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/Drawer>

## Definition

party that requires a drawee to pay either a third party or themselves with respect to a bill of exchange

## Relationships

- **Subclass of**: [Obligee](/concepts/fibo/FND/Agreements/Agreements/Obligee.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N512375935eba428e8bb061de76f5a9eb`

## Annotations

- **label**: drawer
- **definition**: party that requires a drawee to pay either a third party or themselves with respect to a bill of exchange

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
