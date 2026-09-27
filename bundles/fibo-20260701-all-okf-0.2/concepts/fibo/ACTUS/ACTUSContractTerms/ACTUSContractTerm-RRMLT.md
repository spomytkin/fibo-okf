---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - RRMLT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: rateMultiplier
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'Interest rate multiplier. A typical rate resetting rule is LIBOR plus x basis point where x represents the interest
      rate spread.


      However, in some cases like reverse or super floater contracts an additional rate multiplier applies. In this case,
      the new rate is determined as: IPNR after rate reset = Rate selected from the market object * RRMLT + RRSP.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: RRMLT
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Rate Multiplier
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRMLT
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - RRMLT
type: Ontology Individual
---

# ACTUS contract term - RRMLT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-RRMLT>

## Relationships

- **Related to**: [ACTUSContractTermGroup-RateReset](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-RateReset.md)

## Annotations

- **label**: ACTUS contract term - RRMLT
- **hasParameterName**: rateMultiplier
- **hasDescription**: Interest rate multiplier. A typical rate resetting rule is LIBOR plus x basis point where x represents the interest rate spread.  However, in some cases like reverse or super floater contracts an additional rate multiplier applies. In this case, the new rate is determined as: IPNR after rate reset = Rate selected from the market object * RRMLT + RRSP.
- **hasTag**: RRMLT
- **hasTextualName**: Rate Multiplier

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
