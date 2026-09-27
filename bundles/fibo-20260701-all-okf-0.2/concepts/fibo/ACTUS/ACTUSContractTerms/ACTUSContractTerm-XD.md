---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - XD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: exerciseDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Date of exercising a contingent event/obligation such as a forward condition, optionality etc. The Exercise date
      marks the observed timestamp of fixing the contingent event and respective payment obligation not necessarily the timestamp
      of settling the obligation.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: XD
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Exercise Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-XD
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - XD
type: Ontology Individual
---

# ACTUS contract term - XD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-XD>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Settlement](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement.md)

## Annotations

- **label**: ACTUS contract term - XD
- **hasParameterName**: exerciseDate
- **hasDescription**: Date of exercising a contingent event/obligation such as a forward condition, optionality etc. The Exercise date marks the observed timestamp of fixing the contingent event and respective payment obligation not necessarily the timestamp of settling the obligation.
- **hasTag**: XD
- **hasTextualName**: Exercise Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
