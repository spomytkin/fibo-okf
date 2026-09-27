---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - MRVM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: variationMargin
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "MRVM reflects the accrued but not yet paid margin as per SD. \n\nOpen traded positions are revalued by the exchange\
      \ at the end of every trading day using mark-to-market valuation. Often clearing members do not credit or debit their\
      \ clients daily with MRVM, but rather use a Maintenance Margin. If the balance falls outside MRMML (and MRMMU), then\
      \ capital must be added (is refunded) to reach the original margin amount MRIM. We can also say that MVO+MRVM is equal\
      \ to the reference value as per last margin update."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: MRVM
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Variation Margin
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Margining.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Margining
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-MRVM
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - MRVM
type: Ontology Individual
---

# ACTUS contract term - MRVM

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-MRVM>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Margining](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Margining.md)

## Annotations

- **label**: ACTUS contract term - MRVM
- **hasParameterName**: variationMargin
- **hasDescription**: MRVM reflects the accrued but not yet paid margin as per SD.   Open traded positions are revalued by the exchange at the end of every trading day using mark-to-market valuation. Often clearing members do not credit or debit their clients daily with MRVM, but rather use a Maintenance Margin. If the balance falls outside MRMML (and MRMMU), then capital must be added (is refunded) to reach the original margin amount MRIM. We can also say that MVO+MRVM is equal to the reference value as per last margin update.
- **hasTag**: MRVM
- **hasTextualName**: Variation Margin

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
