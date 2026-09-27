---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - IPCB
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: interestCalculationBase
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "This is important for amortizing instruments. The basis of interest calculation is normally the notional outstanding\
      \ amount as per SD. This is considered the fair basis and in many countries the only legal basis. If NULL or NTSD is\
      \ selected, this is the case. \n\nAlternative bases (normally in order to favor the lending institution) are found.\
      \ In the extreme case the original balance (PCDD=NT+PDCDD) never gets adjusted. In this case PCDD must be chosen. \n\
      \nAn intermediate case exist wherre balances do get adjusted, however with lags. In this case NTL mut be selected and\
      \ anchor dates and cycles must be set."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: IPCB
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Interest Calculation Base
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPCB
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - IPCB
type: Ontology Individual
---

# ACTUS contract term - IPCB

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPCB>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Interest](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md)

## Annotations

- **label**: ACTUS contract term - IPCB
- **hasParameterName**: interestCalculationBase
- **hasDescription**: This is important for amortizing instruments. The basis of interest calculation is normally the notional outstanding amount as per SD. This is considered the fair basis and in many countries the only legal basis. If NULL or NTSD is selected, this is the case.   Alternative bases (normally in order to favor the lending institution) are found. In the extreme case the original balance (PCDD=NT+PDCDD) never gets adjusted. In this case PCDD must be chosen.   An intermediate case exist wherre balances do get adjusted, however with lags. In this case NTL mut be selected and anchor dates and cycles must be set.
- **hasTag**: IPCB
- **hasTextualName**: Interest Calculation Base

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
