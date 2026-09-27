---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - RRPNT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: cyclePointOfRateReset
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Normally rates get reset at the beginning of any resetting cycles. There are contracts where the rate is not set
      at the beginning but at the end of the cycle and then applied to the previous cycle (post-fixing); in other words the
      rate applies before it is fixed. Hence, the new rate is not known during the entire cycle where it applies. Therefore,
      the rate will be applied backwards at the end of the cycle. This happens through a correction of interest accrued.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: RRPNT
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Cycle Point Of Rate Reset
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRPNT
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - RRPNT
type: Ontology Individual
---

# ACTUS contract term - RRPNT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRPNT>

## Relationships

- **Related to**: [ACTUSContractTermGroup-RateReset](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md)

## Annotations

- **label**: ACTUS contract term - RRPNT
- **hasParameterName**: cyclePointOfRateReset
- **hasDescription**: Normally rates get reset at the beginning of any resetting cycles. There are contracts where the rate is not set at the beginning but at the end of the cycle and then applied to the previous cycle (post-fixing); in other words the rate applies before it is fixed. Hence, the new rate is not known during the entire cycle where it applies. Therefore, the rate will be applied backwards at the end of the cycle. This happens through a correction of interest accrued.
- **hasTag**: RRPNT
- **hasTextualName**: Cycle Point Of Rate Reset

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
