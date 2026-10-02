---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - DQP
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: delinquencyPeriod
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: If real payment happens after scheduled payment date plus DLP, then the counterparty is in technical default. This
      means that the creditor legally has the right to declare default of the debtor.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: DQP
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Delinquency Period
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-DQP
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - DQP
type: Ontology Individual
---

# ACTUS contract term - DQP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-DQP>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Counterparty](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md)

## Annotations

- **label**: ACTUS contract term - DQP
- **hasParameterName**: delinquencyPeriod
- **hasDescription**: If real payment happens after scheduled payment date plus DLP, then the counterparty is in technical default. This means that the creditor legally has the right to declare default of the debtor.
- **hasTag**: DQP
- **hasTextualName**: Delinquency Period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
