---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: representation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual element that is a statement made by a party to the contract, before or at the time of making the contract,
      in regard to some fact, circumstance, or state of affairs pertinent to the contract, which the counterparty(ies) rely
      on, or is influential in bringing about the contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A party may later claim misrepresentation if a false representation has been made. They may be entitled to rescind
      the contract, which means that the contract would be set aside and the receiving party may also be entitled to damages
      to put them back into the position they would have been had the contract never been entered into.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Representation
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: representation
type: Ontology Class
---

# representation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Representation>

## Definition

contractual element that is a statement made by a party to the contract, before or at the time of making the contract, in regard to some fact, circumstance, or state of affairs pertinent to the contract, which the counterparty(ies) rely on, or is influential in bringing about the contract

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label** (en): representation
- **definition** (en): contractual element that is a statement made by a party to the contract, before or at the time of making the contract, in regard to some fact, circumstance, or state of affairs pertinent to the contract, which the counterparty(ies) rely on, or is influential in bringing about the contract
- **explanatoryNote**: A party may later claim misrepresentation if a false representation has been made. They may be entitled to rescind the contract, which means that the contract would be set aside and the receiving party may also be entitled to damages to put them back into the position they would have been had the contract never been entered into.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
