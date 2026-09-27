---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - RRSP
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: rateSpread
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "Interest rate spread. A typical rate resetting rule is LIBOR plus x basis point where x represents the interest\
      \ rate spread. \n\nThe following equation can be taken if RRMLT is not set: IPNR after rate reset = Rate selected from\
      \ the market object + RRSP."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: RRSP
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Rate Spread
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRSP
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - RRSP
type: Ontology Individual
---

# ACTUS contract term - RRSP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRSP>

## Relationships

- **Related to**: [ACTUSContractTermGroup-RateReset](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md)

## Annotations

- **label**: ACTUS contract term - RRSP
- **hasParameterName**: rateSpread
- **hasDescription**: Interest rate spread. A typical rate resetting rule is LIBOR plus x basis point where x represents the interest rate spread.   The following equation can be taken if RRMLT is not set: IPNR after rate reset = Rate selected from the market object + RRSP.
- **hasTag**: RRSP
- **hasTextualName**: Rate Spread

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
