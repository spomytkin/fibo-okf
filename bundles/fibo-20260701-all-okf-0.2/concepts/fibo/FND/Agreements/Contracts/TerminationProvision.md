---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: termination provision
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual element that specifies the circumstances under which the parties can dissolve their legal relationship
      and discontinue the fulfillment of their obligations under the contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Common reasons for termination include mutual consent, certain notices, breach or failure of a precedent or condition,
      insolvency, change in control, the occurrence of certain events, and court orders that prohibit continuation of the
      contract. Termination provisions may include whether they are mutual or unilateral, and may include rights with respect
      to any cure.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/TerminationProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: termination provision
type: Ontology Class
---

# termination provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/TerminationProvision>

## Definition

contractual element that specifies the circumstances under which the parties can dissolve their legal relationship and discontinue the fulfillment of their obligations under the contract

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label** (en): termination provision
- **definition** (en): contractual element that specifies the circumstances under which the parties can dissolve their legal relationship and discontinue the fulfillment of their obligations under the contract
- **explanatoryNote**: Common reasons for termination include mutual consent, certain notices, breach or failure of a precedent or condition, insolvency, change in control, the occurrence of certain events, and court orders that prohibit continuation of the contract. Termination provisions may include whether they are mutual or unilateral, and may include rights with respect to any cure.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
