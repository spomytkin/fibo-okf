---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - OPCL
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: cycleOfOptionality
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'Cycle according to which the option exercise date schedule will be calculated.


      OPCL can be NULL for American Options or Prepayment Optionality in which case the optionality period starts at OPANX
      and ends at OPXED (for american options) or MD (in case of prepayment optionality).


      The interval will be adjusted yet by EOMC and BDC.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: OPCL
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Cycle Of Optionality
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-OPCL
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - OPCL
type: Ontology Individual
---

# ACTUS contract term - OPCL

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-OPCL>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Optionality](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality.md)

## Annotations

- **label**: ACTUS contract term - OPCL
- **hasParameterName**: cycleOfOptionality
- **hasDescription**: Cycle according to which the option exercise date schedule will be calculated.  OPCL can be NULL for American Options or Prepayment Optionality in which case the optionality period starts at OPANX and ends at OPXED (for american options) or MD (in case of prepayment optionality).  The interval will be adjusted yet by EOMC and BDC.
- **hasTag**: OPCL
- **hasTextualName**: Cycle Of Optionality

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
