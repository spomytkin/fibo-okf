---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - PFL
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '3'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: payFirstLeg
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is split into two terms in the JSON version, which we followed herein. It is ambiguous in the online data
      dictionary.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Contract creator pays the first leg.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: PFL
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Pay First Leg
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-PFL
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - PFL
type: Ontology Individual
---

# ACTUS contract term - PFL

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-PFL>

## Annotations

- **label**: ACTUS contract term - PFL
- **hasOptionSequenceNumber**: 3
- **hasParameterName**: payFirstLeg
- **explanatoryNote**: This is split into two terms in the JSON version, which we followed herein. It is ambiguous in the online data dictionary.
- **hasDescription**: Contract creator pays the first leg.
- **hasTag**: PFL
- **hasTextualName**: Pay First Leg

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
