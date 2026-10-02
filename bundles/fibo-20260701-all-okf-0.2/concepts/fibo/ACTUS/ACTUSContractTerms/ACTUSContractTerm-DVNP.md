---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - DVNP
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: nextDividendPaymentAmount
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "Defines the next dividend payment (amount) whereas the date of dividend payment is defined through the DVANX/DVCL\
      \ pair. \n If DVCL is defined, then this amount will be used as dividend payment for each future dividend payment date."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: DVNP
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Next Dividend Payment Amount
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Dividend.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Dividend
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-DVNP
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - DVNP
type: Ontology Individual
---

# ACTUS contract term - DVNP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-DVNP>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Dividend](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Dividend.md)

## Annotations

- **label**: ACTUS contract term - DVNP
- **hasParameterName**: nextDividendPaymentAmount
- **hasDescription**: Defines the next dividend payment (amount) whereas the date of dividend payment is defined through the DVANX/DVCL pair.   If DVCL is defined, then this amount will be used as dividend payment for each future dividend payment date.
- **hasTag**: DVNP
- **hasTextualName**: Next Dividend Payment Amount

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
