---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collateral agreement that grants a financial interest in some collateral to a party that is not an owner of that
      collateral, specifying terms including relative duties and rights, over and above those specified in the primary contract,
      regarding the disposition of the asset used as collateral
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include deeds of trust and uniform commercial code (UCC) agreements.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 20022
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LenderLienPosition
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OwnershipInterest
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/CollateralAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CollateralAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SecurityAgreement
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: security agreement
type: Ontology Class
---

# security agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SecurityAgreement>

## Definition

collateral agreement that grants a financial interest in some collateral to a party that is not an owner of that collateral, specifying terms including relative duties and rights, over and above those specified in the primary contract, regarding the disposition of the asset used as collateral

## Relationships

- **Subclass of**: [CollateralAgreement](/concepts/fibo/FND/Agreements/Contracts/CollateralAgreement.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [LenderLienPosition](/concepts/fibo/LOAN/LoansGeneral/Loans/LenderLienPosition.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [OwnershipInterest](/concepts/fibo/LOAN/LoansGeneral/Loans/OwnershipInterest.md)

## Annotations

- **label**: security agreement
- **definition**: collateral agreement that grants a financial interest in some collateral to a party that is not an owner of that collateral, specifying terms including relative duties and rights, over and above those specified in the primary contract, regarding the disposition of the asset used as collateral
- **example**: Examples include deeds of trust and uniform commercial code (UCC) agreements.
- **adaptedFrom**: ISO 20022

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
