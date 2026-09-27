---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: disclosure provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual provision that outlines the requirements and responsibilities of one or both parties to reveal certain
      information to each other
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Disclosure provisions are crucial in ensuring transparency, mitigating risks, and maintaining trust between the
      parties. Typical elements of a disclosure provision include (1) scope - defining the kind of information that must be
      disclosed, (2) materiality - which usually states that only information material to the agreement must be disclosed,
      (3) timing - specifying when such disclosures must be made, (4) ongoing requirements - outlining whether or not disclosures
      any time significant changes or new information must be made available over some period of time, (5) method - specifying
      how such disclosures must be made, for example, in writing, (6) exclusions - information that is explicitly out of scope
      with respect to disclosure requirements, (7) confidentiality - restrictions related to whether or not the information
      is confidential and on how it may be used, and (8) penalities - specifying consequences for failing to disclose relevant
      information.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: With respect to contracts, failure to disclose key details can lead to breaches of contract or claims of misrepresentation.
      Disclosure requirements are typically specific to the nature of the contract and jurisdiction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: disclosure provision
type: Ontology Class
---

# disclosure provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision>

## Definition

contractual provision that outlines the requirements and responsibilities of one or both parties to reveal certain information to each other

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label** (en): disclosure provision
- **definition**: contractual provision that outlines the requirements and responsibilities of one or both parties to reveal certain information to each other
- **explanatoryNote**: Disclosure provisions are crucial in ensuring transparency, mitigating risks, and maintaining trust between the parties. Typical elements of a disclosure provision include (1) scope - defining the kind of information that must be disclosed, (2) materiality - which usually states that only information material to the agreement must be disclosed, (3) timing - specifying when such disclosures must be made, (4) ongoing requirements - outlining whether or not disclosures any time significant changes or new information must be made available over some period of time, (5) method - specifying how such disclosures must be made, for example, in writing, (6) exclusions - information that is explicitly out of scope with respect to disclosure requirements, (7) confidentiality - restrictions related to whether or not the information is confidential and on how it may be used, and (8) penalities - specifying consequences for failing to disclose relevant information.
- **explanatoryNote**: With respect to contracts, failure to disclose key details can lead to breaches of contract or claims of misrepresentation. Disclosure requirements are typically specific to the nature of the contract and jurisdiction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
