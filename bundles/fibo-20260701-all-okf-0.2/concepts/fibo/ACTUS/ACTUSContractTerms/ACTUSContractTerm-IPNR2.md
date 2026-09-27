---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - IPNR2
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: nominalInterestRate2
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "The nominal interest rate which will be used to calculate accruals and the next interest payment at the next IP\
      \ date on the second leg (the one not mentioned in CNTRL) of a plain vanilla swap. The relevant time period is a function\
      \ of IPDC. \n\nIt is periodically updated per SD."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: IPNR2
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Nominal Interest Rate 2
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPNR2
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - IPNR2
type: Ontology Individual
---

# ACTUS contract term - IPNR2

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPNR2>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Interest](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md)

## Annotations

- **label**: ACTUS contract term - IPNR2
- **hasParameterName**: nominalInterestRate2
- **hasDescription**: The nominal interest rate which will be used to calculate accruals and the next interest payment at the next IP date on the second leg (the one not mentioned in CNTRL) of a plain vanilla swap. The relevant time period is a function of IPDC.   It is periodically updated per SD.
- **hasTag**: IPNR2
- **hasTextualName**: Nominal Interest Rate 2

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
