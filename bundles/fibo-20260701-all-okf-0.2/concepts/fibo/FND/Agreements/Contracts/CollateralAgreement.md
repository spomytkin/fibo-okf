---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collateral agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: written contract related to another contract designed to provide clarity and additional protection for all parties
      involved, that is separate from the primary contract and that can be independently enforced
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples may be related to leases, to clarify responsibilities with respect to maintance and repair, to partnerships,
      clarifying how disputes should be resolved, loan agreements such as deeds of trust, covering the conditions under which
      the collateral would be forfeited, and uniform commercial code (UCC) agreements.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In cases where there are discrepancies between the collateral agreement and primary contract, the primary contract,
      which may be a master agreement, for example, takes precedence.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isSubordinateTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasEstimatedValue
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CollateralAgreement
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: collateral agreement
type: Ontology Class
---

# collateral agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CollateralAgreement>

## Definition

written contract related to another contract designed to provide clarity and additional protection for all parties involved, that is separate from the primary contract and that can be independently enforced

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: min qualified cardinality 0 of type [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)
- **[isSubordinateTo](/concepts/fibo/FND/Agreements/Contracts/isSubordinateTo.md)**: some values from of type [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)
- **[hasEstimatedValue](/concepts/fibo/FND/Arrangements/Assessments/hasEstimatedValue.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: collateral agreement
- **definition**: written contract related to another contract designed to provide clarity and additional protection for all parties involved, that is separate from the primary contract and that can be independently enforced
- **example**: Examples may be related to leases, to clarify responsibilities with respect to maintance and repair, to partnerships, clarifying how disputes should be resolved, loan agreements such as deeds of trust, covering the conditions under which the collateral would be forfeited, and uniform commercial code (UCC) agreements.
- **explanatoryNote**: In cases where there are discrepancies between the collateral agreement and primary contract, the primary contract, which may be a master agreement, for example, takes precedence.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
