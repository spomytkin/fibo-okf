---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - NPD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: nonPerformingDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: The date of the (uncovered) payment event responsible for the current value of the Contract Performance attribute.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: NPD
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Non Performing Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-NPD
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - NPD
type: Ontology Individual
---

# ACTUS contract term - NPD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-NPD>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Counterparty](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md)

## Annotations

- **label**: ACTUS contract term - NPD
- **hasParameterName**: nonPerformingDate
- **hasDescription**: The date of the (uncovered) payment event responsible for the current value of the Contract Performance attribute.
- **hasTag**: NPD
- **hasTextualName**: Non Performing Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
