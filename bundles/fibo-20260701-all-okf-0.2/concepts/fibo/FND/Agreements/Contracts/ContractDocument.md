---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract document
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal document that records the formal terms and conditions of some contract
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: Written here does not necessarily mean a paper document but includes situations in which the contract is expressed
      electronically, whether as an electronic representation of a formal document such as in PDF form or as an electronic
      message, provided in the latter case that the message is expressly given formal contractual standing, for example as
      indicated in a separate covering agreement between the parties.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/records
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/LegalDocument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractDocument
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: contract document
type: Ontology Class
---

# contract document

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractDocument>

## Definition

legal document that records the formal terms and conditions of some contract

## Relationships

- **Subclass of**: [LegalDocument](<https://www.omg.org/spec/Commons/Documents/LegalDocument>)

## Constraints

- **[records](<https://www.omg.org/spec/Commons/Documents/records>)**: some values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Annotations

- **label**: contract document
- **definition**: legal document that records the formal terms and conditions of some contract
- **scopeNote**: Written here does not necessarily mean a paper document but includes situations in which the contract is expressed electronically, whether as an electronic representation of a formal document such as in PDF form or as an electronic message, provided in the latter case that the message is expressly given formal contractual standing, for example as indicated in a separate covering agreement between the parties.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
