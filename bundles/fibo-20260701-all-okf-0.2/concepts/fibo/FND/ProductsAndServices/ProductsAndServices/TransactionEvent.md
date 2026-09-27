---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any sale, assignment, lease, license, loan, advance, contribution, or other transfer of any interest in or right
      to use any property (tangible or intangible) or money, however that transaction is effected, and regardless of whether
      the terms of the transaction are formally documented
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionEvent
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: transaction event
type: Ontology Class
---

# transaction event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionEvent>

## Definition

any sale, assignment, lease, license, loan, advance, contribution, or other transfer of any interest in or right to use any property (tangible or intangible) or money, however that transaction is effected, and regardless of whether the terms of the transaction are formally documented

## Relationships

- **Subclass of**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Constraints

- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: min qualified cardinality 0 of type [TransactionConfirmation](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation.md)

## Annotations

- **label**: transaction event
- **definition**: any sale, assignment, lease, license, loan, advance, contribution, or other transfer of any interest in or right to use any property (tangible or intangible) or money, however that transaction is effected, and regardless of whether the terms of the transaction are formally documented

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
