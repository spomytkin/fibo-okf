---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund depositary
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The party that holds and safeguards holdings owned by a fund. It is also responsible for compliance of the portfolio
      with legal ratios etc.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The depository may delegate custody to another entity (custodian). Definition origin:EFAMA DD
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/providesDepositaryServiceFor
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund depositary
type: Ontology Class
---

# fund depositary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary>

## Definition

The party that holds and safeguards holdings owned by a fund. It is also responsible for compliance of the portfolio with legal ratios etc.

## Relationships

- **Subclass of**: [FundsProcessingParty](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md)

## Constraints

- **[providesDepositaryServiceFor](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/providesDepositaryServiceFor.md)**: some values from of type [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Annotations

- **label** (en): fund depositary
- **definition** (en): The party that holds and safeguards holdings owned by a fund. It is also responsible for compliance of the portfolio with legal ratios etc.
- **explanatoryNote** (en): The depository may delegate custody to another entity (custodian). Definition origin:EFAMA DD

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
