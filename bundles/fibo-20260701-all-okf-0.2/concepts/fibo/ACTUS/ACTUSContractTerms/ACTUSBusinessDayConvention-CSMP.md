---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS business day convention - CSMP
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: convention that a scheduled date will be calculated from a formula, coupon schedule, or tenor first, then if it
      falls on a non-business date will be shifted to the first preceding day that is a business day unless that day falls
      in the prior calendar month, in which case that date will be the first subsequent day that is a calendar date
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CSMP
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Calculate/Shift modified preceding
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSBusinessDayConvention
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSBusinessDayConvention-CSMP
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS business day convention - CSMP
type: Ontology Individual
---

# ACTUS business day convention - CSMP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSBusinessDayConvention-CSMP>

## Annotations

- **label**: ACTUS business day convention - CSMP
- **hasDescription**: convention that a scheduled date will be calculated from a formula, coupon schedule, or tenor first, then if it falls on a non-business date will be shifted to the first preceding day that is a business day unless that day falls in the prior calendar month, in which case that date will be the first subsequent day that is a calendar date
- **hasTag**: CSMP
- **hasTextualName**: Calculate/Shift modified preceding

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
