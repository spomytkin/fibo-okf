---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - FER
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: feeRate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Rate of Fee which is a percentage of the underlying or FER is an absolute amount. For all contracts where FEB does
      not apply (cf. business rules), FER is interpreted as an absolute amount.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: FER
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Fee Rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Fees.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Fees
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-FER
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - FER
type: Ontology Individual
---

# ACTUS contract term - FER

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-FER>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Fees](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Fees.md)

## Annotations

- **label**: ACTUS contract term - FER
- **hasParameterName**: feeRate
- **hasDescription**: Rate of Fee which is a percentage of the underlying or FER is an absolute amount. For all contracts where FEB does not apply (cf. business rules), FER is interpreted as an absolute amount.
- **hasTag**: FER
- **hasTextualName**: Fee Rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
