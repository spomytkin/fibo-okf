---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: r e a claim
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Some imbalance, at a given point in time, between the respective rights and obligations of two parties with respect
      to one another.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalConstruct
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/isImbalanceIn
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/REAClaim
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: r e a claim
type: Ontology Class
---

# r e a claim

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/REAClaim>

## Definition

Some imbalance, at a given point in time, between the respective rights and obligations of two parties with respect to one another.

## Constraints

- **[isImbalanceIn](/concepts/fibo/FND/TransactionsExt/REATransactions/isImbalanceIn.md)**: some values from of type [LegalConstruct](/concepts/fibo/FND/Law/LegalCapacity/LegalConstruct.md)

## Annotations

- **label** (en): r e a claim
- **definition** (en): Some imbalance, at a given point in time, between the respective rights and obligations of two parties with respect to one another.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
