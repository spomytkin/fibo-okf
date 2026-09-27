---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - RRFIX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: fixingPeriod
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Interest rate resets (adjustments) are usually fixed one or two days (usually Business Days) before the new rate
      applies (defined by the rate reset schedule). This field holds the period between fixing and application of a rate.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: RRFIX
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Fixing Period
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRFIX
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - RRFIX
type: Ontology Individual
---

# ACTUS contract term - RRFIX

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRFIX>

## Relationships

- **Related to**: [ACTUSContractTermGroup-RateReset](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md)

## Annotations

- **label**: ACTUS contract term - RRFIX
- **hasParameterName**: fixingPeriod
- **hasDescription**: Interest rate resets (adjustments) are usually fixed one or two days (usually Business Days) before the new rate applies (defined by the rate reset schedule). This field holds the period between fixing and application of a rate.
- **hasTag**: RRFIX
- **hasTextualName**: Fixing Period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
