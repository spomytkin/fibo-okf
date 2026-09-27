---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - ARRATE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: arrayRate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'For array-type rate reset schedules, this attribute represents either an interest rate (corresponding to IPNR)
      or a spread (corresponding to RRSP). Which case applies depends on the attribute ARFIXVAR: if ARFIXVAR=FIX then it represents
      the new IPNR and if ARFIXVAR=VAR then the applicable RRSP.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: ARRATE
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Array Rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-ARRATE
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - ARRATE
type: Ontology Individual
---

# ACTUS contract term - ARRATE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-ARRATE>

## Relationships

- **Related to**: [ACTUSContractTermGroup-RateReset](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md)

## Annotations

- **label**: ACTUS contract term - ARRATE
- **hasParameterName**: arrayRate
- **hasDescription**: For array-type rate reset schedules, this attribute represents either an interest rate (corresponding to IPNR) or a spread (corresponding to RRSP). Which case applies depends on the attribute ARFIXVAR: if ARFIXVAR=FIX then it represents the new IPNR and if ARFIXVAR=VAR then the applicable RRSP.
- **hasTag**: ARRATE
- **hasTextualName**: Array Rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
