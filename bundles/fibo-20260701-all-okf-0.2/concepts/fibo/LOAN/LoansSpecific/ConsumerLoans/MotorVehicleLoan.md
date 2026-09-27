---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: motor vehicle loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collateralized, simple-interest loan that is repaid in monthly installments over a period of typically three to
      five years, for the purpose of purchasing a vehicle
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 12 CFR § 228.12, https://www.law.cornell.edu/cfr/text/12/228.12
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Many lenders will only approve auto loans for vehicles (i.e., cars, trucks) that are a certain age (typically 5
      years or less) due to depreciation of the value of the vehicle. Because an auto loan is a 'secured' type of loan, the
      vehicle that is being financed is used as collateral (i.e. if the borrower fails to repay the loan, the vehicle may
      be seized by the lender).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: auto loan
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PhysicalCollateral
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/CollateralizedLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CollateralizedLoan
  - concept: /concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/MotorVehicleLoan
sources:
- id: fibo-source-7c7642cd54
  resource: references/fibo/LOAN/LoansSpecific/ConsumerLoans.rdf
  sha256: 7c7642cd546c2c1de619d2ea9b384b314886dedf7c8601dab9a46870d0e591d7
  title: FIBO source LOAN/LoansSpecific/ConsumerLoans.rdf
title: motor vehicle loan
type: Ontology Class
---

# motor vehicle loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/MotorVehicleLoan>

## Definition

collateralized, simple-interest loan that is repaid in monthly installments over a period of typically three to five years, for the purpose of purchasing a vehicle

## Relationships

- **Subclass of**: [CollateralizedLoan](/concepts/fibo/LOAN/LoansGeneral/Loans/CollateralizedLoan.md)
- **Subclass of**: [SecuredConsumerLoan](/concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: some values from of type [PhysicalCollateral](/concepts/fibo/FBC/DebtAndEquities/Debt/PhysicalCollateral.md)

## Annotations

- **label** (en): motor vehicle loan
- **definition** (en): collateralized, simple-interest loan that is repaid in monthly installments over a period of typically three to five years, for the purpose of purchasing a vehicle
- **adaptedFrom** (en): 12 CFR § 228.12, https://www.law.cornell.edu/cfr/text/12/228.12
- **explanatoryNote** (en): Many lenders will only approve auto loans for vehicles (i.e., cars, trucks) that are a certain age (typically 5 years or less) due to depreciation of the value of the vehicle. Because an auto loan is a 'secured' type of loan, the vehicle that is being financed is used as collateral (i.e. if the borrower fails to repay the loan, the vehicle may be seized by the lender).
- **synonym** (en): auto loan

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
