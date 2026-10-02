---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - UDLM
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '12'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: underlyingMinus
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is missing from the online data dictionary.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Contract represents the underlying to a composed contract. Role of the underlying is derived from the parent. When
      considered a standalone contract the underlying's creator takes the liability side.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: UDLM
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Underlying Minus
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-UDLM
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - UDLM
type: Ontology Individual
---

# ACTUS contract term - UDLM

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier-UDLM>

## Annotations

- **label**: ACTUS contract term - UDLM
- **hasOptionSequenceNumber**: 12
- **hasParameterName**: underlyingMinus
- **explanatoryNote**: This is missing from the online data dictionary.
- **hasDescription**: Contract represents the underlying to a composed contract. Role of the underlying is derived from the parent. When considered a standalone contract the underlying's creator takes the liability side.
- **hasTag**: UDLM
- **hasTextualName**: Underlying Minus

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
