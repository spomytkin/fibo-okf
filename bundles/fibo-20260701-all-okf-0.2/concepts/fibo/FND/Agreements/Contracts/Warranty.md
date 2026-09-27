---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: warranty
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual element that is a statement of fact
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If a warranty is determined to be false, the receiving party has a claim for breach of contract. If it is a fundamental
      breach the receiving party may have the right to terminate the contact in addition to a claim for damages. However,
      unlike a claim for misrepresentation, the contract may not necessarily be voided in its entirety as a consequence.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Warranty
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: warranty
type: Ontology Class
---

# warranty

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Warranty>

## Definition

contractual element that is a statement of fact

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label** (en): warranty
- **definition** (en): contractual element that is a statement of fact
- **explanatoryNote** (en): If a warranty is determined to be false, the receiving party has a claim for breach of contract. If it is a fundamental breach the receiving party may have the right to terminate the contact in addition to a claim for damages. However, unlike a claim for misrepresentation, the contract may not necessarily be voided in its entirety as a consequence.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
