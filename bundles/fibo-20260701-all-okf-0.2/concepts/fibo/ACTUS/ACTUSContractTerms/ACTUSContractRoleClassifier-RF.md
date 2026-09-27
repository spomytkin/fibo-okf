---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - RF
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '4'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: receiveFix
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is missing from the online data dictionary, merged with RFL and thus ambiguous.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Contract creator receives the fixed leg.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: RF
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Receive Fix
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-RF
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - RF
type: Ontology Individual
---

# ACTUS contract term - RF

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-RF>

## Annotations

- **label**: ACTUS contract term - RF
- **hasOptionSequenceNumber**: 4
- **hasParameterName**: receiveFix
- **explanatoryNote**: This is missing from the online data dictionary, merged with RFL and thus ambiguous.
- **hasDescription**: Contract creator receives the fixed leg.
- **hasTag**: RF
- **hasTextualName**: Receive Fix

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
