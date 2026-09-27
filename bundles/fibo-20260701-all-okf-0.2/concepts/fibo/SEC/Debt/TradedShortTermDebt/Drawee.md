---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: drawee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that is required to pay the amount stated on the bill of exchange to the payee
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N92f17103944f4213bd5d1dad2b994db0
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payer
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/Drawee
sources:
- id: fibo-source-5edf240c05
  resource: references/fibo/SEC/Debt/TradedShortTermDebt.rdf
  sha256: 5edf240c05ec5ae1a2890d6bacd728412073d70868c0908cad8aaea54d9d21bf
  title: FIBO source SEC/Debt/TradedShortTermDebt.rdf
title: drawee
type: Ontology Class
---

# drawee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/Drawee>

## Definition

party that is required to pay the amount stated on the bill of exchange to the payee

## Relationships

- **Subclass of**: [Payer](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N92f17103944f4213bd5d1dad2b994db0`

## Annotations

- **label**: drawee
- **definition**: party that is required to pay the amount stated on the bill of exchange to the payee

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
