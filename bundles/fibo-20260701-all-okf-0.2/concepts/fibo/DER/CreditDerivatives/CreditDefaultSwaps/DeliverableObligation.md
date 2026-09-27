---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: deliverable asset
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset that must be delivered as a part of the process of settling a credit default swap
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the reference obligation is a bond, the deliverable asset (obligation) may be a different bond. If it is a loan,
      the deliverable asset may involve assigment of a loan.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: deliverable asset
type: Ontology Class
---

# deliverable asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation>

## Definition

asset that must be delivered as a part of the process of settling a credit default swap

## Relationships

- **Subclass of**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Annotations

- **label** (en): deliverable asset
- **definition** (en): asset that must be delivered as a part of the process of settling a credit default swap
- **explanatoryNote** (en): If the reference obligation is a bond, the deliverable asset (obligation) may be a different bond. If it is a loan, the deliverable asset may involve assigment of a loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
