---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: index-linked bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond whose income may vary over time, because either the coupon rate or principal amount is related to a specific
      index, such as the Consumer Price Index
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
    value: N08e659c56dee4e06b335fa31f422d9eb
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariableIncomeBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableIncomeBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/IndexLinkedBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: index-linked bond
type: Ontology Class
---

# index-linked bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/IndexLinkedBond>

## Definition

bond whose income may vary over time, because either the coupon rate or principal amount is related to a specific index, such as the Consumer Price Index

## Relationships

- **Subclass of**: [VariableIncomeBond](/concepts/fibo/SEC/Debt/Bonds/VariableIncomeBond.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from value `N08e659c56dee4e06b335fa31f422d9eb`

## Annotations

- **label**: index-linked bond
- **definition**: bond whose income may vary over time, because either the coupon rate or principal amount is related to a specific index, such as the Consumer Price Index

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
