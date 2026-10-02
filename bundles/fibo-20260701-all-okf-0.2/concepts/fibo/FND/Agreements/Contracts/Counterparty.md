---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: counterparty
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party to a contract with whom one negotiates on a given agreement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The counterparty is usually the party 'on the other side' of a contract from the perspective of the issuer or holder.
      The term 'counterparty' can refer to any party to an agreement, depending on context.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: counterparty
type: Ontology Class
---

# counterparty

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty>

## Definition

party to a contract with whom one negotiates on a given agreement

## Relationships

- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)

## Annotations

- **label**: counterparty
- **definition**: party to a contract with whom one negotiates on a given agreement
- **explanatoryNote**: The counterparty is usually the party 'on the other side' of a contract from the perspective of the issuer or holder. The term 'counterparty' can refer to any party to an agreement, depending on context.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
