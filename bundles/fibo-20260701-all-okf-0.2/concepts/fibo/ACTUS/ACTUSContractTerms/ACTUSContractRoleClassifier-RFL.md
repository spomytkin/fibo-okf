---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - RFL
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '2'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: receiveFirstLeg1
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is split into two terms in the JSON version, which we followed herein. It is ambiguous in the online data
      dictionary.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Contract creator receives the first leg.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: RFL
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Receive First Leg
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-RFL
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - RFL
type: Ontology Individual
---

# ACTUS contract term - RFL

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-RFL>

## Annotations

- **label**: ACTUS contract term - RFL
- **hasOptionSequenceNumber**: 2
- **hasParameterName**: receiveFirstLeg1
- **explanatoryNote**: This is split into two terms in the JSON version, which we followed herein. It is ambiguous in the online data dictionary.
- **hasDescription**: Contract creator receives the first leg.
- **hasTag**: RFL
- **hasTextualName**: Receive First Leg

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
