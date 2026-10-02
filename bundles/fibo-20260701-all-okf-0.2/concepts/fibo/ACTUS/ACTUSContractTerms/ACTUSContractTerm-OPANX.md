---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - OPANX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: cycleAnchorDateOfOptionality
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "Used for Basic Maturities (such as PAM, RGM, ANN, NGM and their Step-up versions) and American and Bermudan style\
      \ options. \n\n- Basic Maturities: Within the group of these Maturities, it indicates the possibility of prepayments.\
      \ Prepayment features are controlled by Behavior. \n\n- American and Bermudan style Options: Begin of exercise period."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: OPANX
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Cycle Anchor Date Of Optionality
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-OPANX
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - OPANX
type: Ontology Individual
---

# ACTUS contract term - OPANX

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-OPANX>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Optionality](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality.md)

## Annotations

- **label**: ACTUS contract term - OPANX
- **hasParameterName**: cycleAnchorDateOfOptionality
- **hasDescription**: Used for Basic Maturities (such as PAM, RGM, ANN, NGM and their Step-up versions) and American and Bermudan style options.   - Basic Maturities: Within the group of these Maturities, it indicates the possibility of prepayments. Prepayment features are controlled by Behavior.   - American and Bermudan style Options: Begin of exercise period.
- **hasTag**: OPANX
- **hasTextualName**: Cycle Anchor Date Of Optionality

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
