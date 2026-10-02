---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - GRP
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: gracePeriod
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: If real payment happens after scheduled payment date plus GRP, then the payment is in delay.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: GRP
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Grace Period
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-GRP
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - GRP
type: Ontology Individual
---

# ACTUS contract term - GRP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-GRP>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Counterparty](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md)

## Annotations

- **label**: ACTUS contract term - GRP
- **hasParameterName**: gracePeriod
- **hasDescription**: If real payment happens after scheduled payment date plus GRP, then the payment is in delay.
- **hasTag**: GRP
- **hasTextualName**: Grace Period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
