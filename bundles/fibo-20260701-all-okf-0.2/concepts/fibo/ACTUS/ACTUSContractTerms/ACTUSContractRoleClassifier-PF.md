---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - PF
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '5'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: payFix
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is missing from the online data dictionary, merged with PFL and thus ambiguous.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Contract creator pays the fixed leg.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: PF
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Pay Fix
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-PF
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - PF
type: Ontology Individual
---

# ACTUS contract term - PF

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-PF>

## Annotations

- **label**: ACTUS contract term - PF
- **hasOptionSequenceNumber**: 5
- **hasParameterName**: payFix
- **explanatoryNote**: This is missing from the online data dictionary, merged with PFL and thus ambiguous.
- **hasDescription**: Contract creator pays the fixed leg.
- **hasTag**: PF
- **hasTextualName**: Pay Fix

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
