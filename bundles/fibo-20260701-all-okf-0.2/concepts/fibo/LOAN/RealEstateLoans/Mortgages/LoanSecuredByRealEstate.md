---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: Consolidated Reports of Condition and Income for a Bank with Domestic and Foreign Offices - FFIEC 031; Board of
      Governors of the Federal Reserve System OMB Number 7100-0036, Federal Deposit Insurance Corporation OMB Number 3064-0052,
      Office of the Comptroller of the Currency OMB Number 1557-0081, dated 20240930
  - predicate: http://purl.org/dc/terms/source
    value: Instructions for the Preparation of Consolidated Reports of Condition and Income, FFIEC 031 and FFIEC 041, Updated
      March 2023, clause A-91
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan secured by real estate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan that, at origination, is secured wholly or substantially by a lien or liens on real property for which the
      lien or liens are central to the extension of the credit - that is, the borrower would not have been extended credit
      in the same amount or on terms as favorable without the lien or liens on real property
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Examples include (a) Construction, land development, and other land loans: (1) 1-4 family residential construction
      loans, and (2) Other construction loans and all land development and other land loans; (b) Secured by farmland (including
      farm residential and other improvements); (c) Secured by 1-4 family residential properties: (1) Revolving, open-end
      loans secured by 1-4 family residential properties and extended under lines of credit, and (2) Closed-end loans secured
      by 1-4 family residential properties including those secured by first liens and those secured by junior liens; (d) Secured
      by multifamily (5 or more) residential properties; and (e) Secured by nonfarm nonresidential properties: (1) Loans secured
      by owner-occupied nonfarm nonresidential, and (2) Loans secured by other nonfarm nonresidential properties.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In general parlance, loans secured by real estate are often called mortgages or mortgage loans. This usage conflates
      a number of related concepts, which would limit the usability of FIBO for financial institutions and regulators with
      respect to such loans. As described herein, many different kinds of loans can be secured by real estate, including various
      commercial, construction, agricultural, and consumer loans.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the US, to be considered wholly or substantially secured by a lien or liens on real property, the estimated
      value of the real estate collateral at origination (after deducting any more senior liens held by others) must be greater
      than 50 percent of the principal amount of the loan at origination.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The borrower agrees to pay the lender over time, typically in a series of regular payments divided into principal
      and interest. The property then serves as collateral to secure the loan.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasGuarantor
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/UseOfProceedsProvision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Servicer
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isServicedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/assumes
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasOriginatingServiceProvider
    value: N1bf24f65401a46ba9814af4ac080c8e6
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasOriginatorPerson
    value: N3a92b22e4a6f402fa200a99f522fa35d
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/hasInitialFundingDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SecurityAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/CollateralizedLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CollateralizedLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
- id: fibo-source-69fec2eeb0
  resource: references/fibo/LOAN/RealEstateLoans/Mortgages.rdf
  sha256: 69fec2eeb0f7fc099e11c13a9ed3e6b5a1902c2f2a2af30a81282d1f4a6bdfa5
  title: FIBO source LOAN/RealEstateLoans/Mortgages.rdf
title: loan secured by real estate
type: Ontology Class
---

# loan secured by real estate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate>

## Definition

loan that, at origination, is secured wholly or substantially by a lien or liens on real property for which the lien or liens are central to the extension of the credit - that is, the borrower would not have been extended credit in the same amount or on terms as favorable without the lien or liens on real property

## Relationships

- **Subclass of**: [CollateralizedLoan](/concepts/fibo/LOAN/LoansGeneral/Loans/CollateralizedLoan.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: some values from of type [RealProperty](/concepts/fibo/FND/Places/RealProperty/RealProperty.md)
- **[hasGuarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/hasGuarantor.md)**: min qualified cardinality 0 of type [MortgageIndemnityGuarantor](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [DisclosureProvision](/concepts/fibo/FND/Agreements/Contracts/DisclosureProvision.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [UseOfProceedsProvision](/concepts/fibo/FND/Agreements/Contracts/UseOfProceedsProvision.md)
- **[isServicedBy](/concepts/fibo/LOAN/LoansGeneral/Loans/isServicedBy.md)**: min qualified cardinality 0 of type [Servicer](/concepts/fibo/LOAN/LoansGeneral/Loans/Servicer.md)
- **[assumes](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/assumes.md)**: min qualified cardinality 0 of type [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
- **[hasOriginatingServiceProvider](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/hasOriginatingServiceProvider.md)**: some values from value `N1bf24f65401a46ba9814af4ac080c8e6`
- **[hasOriginatorPerson](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/hasOriginatorPerson.md)**: some values from value `N3a92b22e4a6f402fa200a99f522fa35d`
- **[hasInitialFundingDate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/hasInitialFundingDate.md)**: some values from of type [TransactionDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [SecurityAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/SecurityAgreement.md)

## Annotations

- **source**: Consolidated Reports of Condition and Income for a Bank with Domestic and Foreign Offices - FFIEC 031; Board of Governors of the Federal Reserve System OMB Number 7100-0036, Federal Deposit Insurance Corporation OMB Number 3064-0052, Office of the Comptroller of the Currency OMB Number 1557-0081, dated 20240930
- **source**: Instructions for the Preparation of Consolidated Reports of Condition and Income, FFIEC 031 and FFIEC 041, Updated March 2023, clause A-91
- **label**: loan secured by real estate
- **definition**: loan that, at origination, is secured wholly or substantially by a lien or liens on real property for which the lien or liens are central to the extension of the credit - that is, the borrower would not have been extended credit in the same amount or on terms as favorable without the lien or liens on real property
- **example** (en): Examples include (a) Construction, land development, and other land loans: (1) 1-4 family residential construction loans, and (2) Other construction loans and all land development and other land loans; (b) Secured by farmland (including farm residential and other improvements); (c) Secured by 1-4 family residential properties: (1) Revolving, open-end loans secured by 1-4 family residential properties and extended under lines of credit, and (2) Closed-end loans secured by 1-4 family residential properties including those secured by first liens and those secured by junior liens; (d) Secured by multifamily (5 or more) residential properties; and (e) Secured by nonfarm nonresidential properties: (1) Loans secured by owner-occupied nonfarm nonresidential, and (2) Loans secured by other nonfarm nonresidential properties.
- **explanatoryNote** (en): In general parlance, loans secured by real estate are often called mortgages or mortgage loans. This usage conflates a number of related concepts, which would limit the usability of FIBO for financial institutions and regulators with respect to such loans. As described herein, many different kinds of loans can be secured by real estate, including various commercial, construction, agricultural, and consumer loans.
- **explanatoryNote** (en): In the US, to be considered wholly or substantially secured by a lien or liens on real property, the estimated value of the real estate collateral at origination (after deducting any more senior liens held by others) must be greater than 50 percent of the principal amount of the loan at origination.
- **explanatoryNote** (en): The borrower agrees to pay the lender over time, typically in a series of regular payments divided into principal and interest. The property then serves as collateral to secure the loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
