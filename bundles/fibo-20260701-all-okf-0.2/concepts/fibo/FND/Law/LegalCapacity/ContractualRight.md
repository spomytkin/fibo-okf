---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual right
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legally enforceable benefit or entitlement granted to a party within a binding agreement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Contractual rights are established by the terms of a contract, which can be explicit (written) or implied by law,
      industry standards, or consistent practices.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualObligation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/implies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Right.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Right
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualRight
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: contractual right
type: Ontology Class
---

# contractual right

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualRight>

## Definition

legally enforceable benefit or entitlement granted to a party within a binding agreement

## Relationships

- **Subclass of**: [Right](/concepts/fibo/FND/Law/LegalCapacity/Right.md)

## Constraints

- **[implies](/concepts/fibo/FND/Law/LegalCapacity/implies.md)**: some values from of type [ContractualObligation](/concepts/fibo/FND/Law/LegalCapacity/ContractualObligation.md)
- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Annotations

- **label**: contractual right
- **definition**: legally enforceable benefit or entitlement granted to a party within a binding agreement
- **explanatoryNote**: Contractual rights are established by the terms of a contract, which can be explicit (written) or implied by law, industry standards, or consistent practices.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
