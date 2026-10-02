---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CETC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: creditEventTypeCovered
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: The type of credit events covered e.g. in credit enhancement or credit default swap contracts. Only the defined
      credit event types may trigger the protection.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CETC
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Credit Event Type Covered
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CETC
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CETC
type: Ontology Individual
---

# ACTUS contract term - CETC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CETC>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Counterparty](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md)

## Annotations

- **label**: ACTUS contract term - CETC
- **hasParameterName**: creditEventTypeCovered
- **hasDescription**: The type of credit events covered e.g. in credit enhancement or credit default swap contracts. Only the defined credit event types may trigger the protection.
- **hasTag**: CETC
- **hasTextualName**: Credit Event Type Covered

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
