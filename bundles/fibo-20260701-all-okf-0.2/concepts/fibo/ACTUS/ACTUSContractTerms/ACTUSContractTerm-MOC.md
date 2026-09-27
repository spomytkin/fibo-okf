---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - MOC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: marketObjectCode
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Need to investigate what to map to represent the market value for a contract ...
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'Is pointing to the market value at SD (MarketObject).


      Unique codes for market objects must be used.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: MOC
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Market Object Code
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-MOC
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - MOC
type: Ontology Individual
---

# ACTUS contract term - MOC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-MOC>

## Relationships

- **Related to**: [ACTUSContractTermGroup-ContractIdentification](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md)

## Annotations

- **label**: ACTUS contract term - MOC
- **hasParameterName**: marketObjectCode
- **explanatoryNote**: Need to investigate what to map to represent the market value for a contract ...
- **hasDescription**: Is pointing to the market value at SD (MarketObject).  Unique codes for market objects must be used.
- **hasTag**: MOC
- **hasTextualName**: Market Object Code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
