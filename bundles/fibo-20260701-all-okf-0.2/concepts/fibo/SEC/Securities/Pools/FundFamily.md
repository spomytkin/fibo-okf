---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund family
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection of managed investments that are all managed by a single investment institution
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/FundFamily
sources:
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: fund family
type: Ontology Class
---

# fund family

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/FundFamily>

## Definition

collection of managed investments that are all managed by a single investment institution

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [ManagedInvestment](/concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: exact qualified cardinality 1 of type [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label**: fund family
- **definition**: collection of managed investments that are all managed by a single investment institution

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
