---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cross default provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract provision that triggers a default under one contract if the borrower defaults on another related obligation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Cross default provisions are commonly found in loans, bond indentures, syndicated loans, and other instruments
      such as certain master agreements (e.g., derivatives transactions master agreements).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/hasDefaultThresholdAmount
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ConditionPrecedent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ConditionPrecedent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/CrossDefaultProvision
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: cross default provision
type: Ontology Class
---

# cross default provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/CrossDefaultProvision>

## Definition

contract provision that triggers a default under one contract if the borrower defaults on another related obligation

## Relationships

- **Subclass of**: [ConditionPrecedent](/concepts/fibo/FND/Agreements/Contracts/ConditionPrecedent.md)

## Constraints

- **[hasDefaultThresholdAmount](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/hasDefaultThresholdAmount.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)

## Annotations

- **label** (en): cross default provision
- **definition**: contract provision that triggers a default under one contract if the borrower defaults on another related obligation
- **explanatoryNote**: Cross default provisions are commonly found in loans, bond indentures, syndicated loans, and other instruments such as certain master agreements (e.g., derivatives transactions master agreements).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
