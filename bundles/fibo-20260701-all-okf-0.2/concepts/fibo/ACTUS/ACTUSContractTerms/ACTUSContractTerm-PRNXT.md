---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - PRNXT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: nextPrincipalRedemptionPayment
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Amount of principal that will be paid during the redemption cycle at the next payment date. For amortizing contracts
      like ANN, NAM, ANX, and NAX this is the total periodic payment amount (sum of interest and principal).
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: PRNXT
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Next Principal Redemption Payment
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PRNXT
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - PRNXT
type: Ontology Individual
---

# ACTUS contract term - PRNXT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PRNXT>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - PRNXT
- **hasParameterName**: nextPrincipalRedemptionPayment
- **hasDescription**: Amount of principal that will be paid during the redemption cycle at the next payment date. For amortizing contracts like ANN, NAM, ANX, and NAX this is the total periodic payment amount (sum of interest and principal).
- **hasTag**: PRNXT
- **hasTextualName**: Next Principal Redemption Payment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
