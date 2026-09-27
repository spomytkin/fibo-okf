---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: shareholder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that owns shares in and has rights and responsibilities with respect to some asset, provided in exchange
      for investment
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The shares represent an ownership interest in a corporation, mutual fund, or partnership, or a unit of ownership
      in a structured product, such as a real estate investment trust.
  - language: en-US
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: stockholder
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner
  - concept: /concepts/fibo/FND/Agreements/Contracts/Counterparty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholder
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
title: shareholder
type: Ontology Class
---

# shareholder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholder>

## Definition

party that owns shares in and has rights and responsibilities with respect to some asset, provided in exchange for investment

## Relationships

- **Subclass of**: [ConstitutionalOwner](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner.md)
- **Subclass of**: [Counterparty](/concepts/fibo/FND/Agreements/Contracts/Counterparty.md)

## Annotations

- **label**: shareholder
- **definition**: party that owns shares in and has rights and responsibilities with respect to some asset, provided in exchange for investment
- **explanatoryNote**: The shares represent an ownership interest in a corporation, mutual fund, or partnership, or a unit of ownership in a structured product, such as a real estate investment trust.
- **synonym** (en-US): stockholder

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
