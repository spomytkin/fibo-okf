---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - FEB
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: feeBasis
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Basis, on which Fee is calculated. For FEB='A', FER is interpreted as an absolute amount to be paid at every FP
      event and for FEB='N', FER represents a rate at which FP amounts accrue on the basis of the contract's NT.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: FEB
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Fee Basis
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Fees.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Fees
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-FEB
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - FEB
type: Ontology Individual
---

# ACTUS contract term - FEB

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-FEB>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Fees](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Fees.md)

## Annotations

- **label**: ACTUS contract term - FEB
- **hasParameterName**: feeBasis
- **hasDescription**: Basis, on which Fee is calculated. For FEB='A', FER is interpreted as an absolute amount to be paid at every FP event and for FEB='N', FER represents a rate at which FP amounts accrue on the basis of the contract's NT.
- **hasTag**: FEB
- **hasTextualName**: Fee Basis

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
