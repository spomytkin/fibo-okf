---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - RRNXT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: nextResetRate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Holds the new rate that has been fixed already (cf. attribute FixingDays) but not applied. This new rate will be
      applied at the next rate reset event (after SD and according to the rate reset schedule). Attention, RRNXT must be set
      to NULL after it is applied.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: RRNXT
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Next Reset Rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRNXT
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - RRNXT
type: Ontology Individual
---

# ACTUS contract term - RRNXT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRNXT>

## Relationships

- **Related to**: [ACTUSContractTermGroup-RateReset](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md)

## Annotations

- **label**: ACTUS contract term - RRNXT
- **hasParameterName**: nextResetRate
- **hasDescription**: Holds the new rate that has been fixed already (cf. attribute FixingDays) but not applied. This new rate will be applied at the next rate reset event (after SD and according to the rate reset schedule). Attention, RRNXT must be set to NULL after it is applied.
- **hasTag**: RRNXT
- **hasTextualName**: Next Reset Rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
