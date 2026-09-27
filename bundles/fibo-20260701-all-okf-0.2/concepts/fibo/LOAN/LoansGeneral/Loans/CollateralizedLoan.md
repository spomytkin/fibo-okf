---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collateralized loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: secured loan that is secured with cash or other acceptable collateral (real property, securities or other assets)
      provided by the borrower as specified in the collateral agreement
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CollateralAgreement
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isPrimaryContractFor
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/SecuredLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/SecuredLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CollateralizedLoan
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: collateralized loan
type: Ontology Class
---

# collateralized loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CollateralizedLoan>

## Definition

secured loan that is secured with cash or other acceptable collateral (real property, securities or other assets) provided by the borrower as specified in the collateral agreement

## Relationships

- **Subclass of**: [SecuredLoan](/concepts/fibo/LOAN/LoansGeneral/Loans/SecuredLoan.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: some values from of type [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)
- **[isPrimaryContractFor](/concepts/fibo/FND/Agreements/Contracts/isPrimaryContractFor.md)**: some values from of type [CollateralAgreement](/concepts/fibo/FND/Agreements/Contracts/CollateralAgreement.md)

## Annotations

- **label** (en): collateralized loan
- **definition** (en): secured loan that is secured with cash or other acceptable collateral (real property, securities or other assets) provided by the borrower as specified in the collateral agreement
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
