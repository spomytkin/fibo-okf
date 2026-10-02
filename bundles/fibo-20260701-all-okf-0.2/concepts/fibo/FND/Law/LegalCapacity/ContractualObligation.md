---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual obligation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legally binding obligation that arises from the terms of a contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Contractual obligations require a party to perform or refrain from performing specific actions, and failure to
      meet an obligation can result in legal consequences.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualRight
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isImpliedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualObligation
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: contractual obligation
type: Ontology Class
---

# contractual obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualObligation>

## Definition

legally binding obligation that arises from the terms of a contract

## Relationships

- **Subclass of**: [LegalObligation](/concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md)

## Constraints

- **[isImpliedBy](/concepts/fibo/FND/Law/LegalCapacity/isImpliedBy.md)**: all values from of type [ContractualRight](/concepts/fibo/FND/Law/LegalCapacity/ContractualRight.md)
- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Annotations

- **label**: contractual obligation
- **definition**: legally binding obligation that arises from the terms of a contract
- **explanatoryNote**: Contractual obligations require a party to perform or refrain from performing specific actions, and failure to meet an obligation can result in legal consequences.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
