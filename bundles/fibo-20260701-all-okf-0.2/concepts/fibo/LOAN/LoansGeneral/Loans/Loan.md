---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt instrument whereby one party extends money or credit to another party (or parties) with the understanding
      that the borrowed money will be repaid according to the terms of the contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasMaturityDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasGuarantor
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasCorrespondingAccount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasThirdParty
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasNegativeAmortization
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasPrincipalAmount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasTotalClosingCosts
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasTotalPointsAndFees
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isInterestOnly
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Servicer
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/isServicedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LenderLienPosition
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanMarketCategory
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: loan
type: Ontology Class
---

# loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan>

## Definition

debt instrument whereby one party extends money or credit to another party (or parties) with the understanding that the borrowed money will be repaid according to the terms of the contract

## Relationships

- **Subclass of**: [CreditAgreementRepaidPeriodically](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)
- **Subclass of**: [DebtInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)

## Constraints

- **[hasMaturityDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasMaturityDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasGuarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/hasGuarantor.md)**: min qualified cardinality 0 of type [Guarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- **[hasCorrespondingAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasCorrespondingAccount.md)**: min qualified cardinality 0 of type [LoanSpecificCustomerAccount](/concepts/fibo/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount.md)
- **[hasThirdParty](/concepts/fibo/FND/Agreements/Contracts/hasThirdParty.md)**: min qualified cardinality 0 of type [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)
- **[hasNegativeAmortization](/concepts/fibo/LOAN/LoansGeneral/Loans/hasNegativeAmortization.md)**: min qualified cardinality 0 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[hasPrincipalAmount](/concepts/fibo/LOAN/LoansGeneral/Loans/hasPrincipalAmount.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasTotalClosingCosts](/concepts/fibo/LOAN/LoansGeneral/Loans/hasTotalClosingCosts.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasTotalPointsAndFees](/concepts/fibo/LOAN/LoansGeneral/Loans/hasTotalPointsAndFees.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isInterestOnly](/concepts/fibo/LOAN/LoansGeneral/Loans/isInterestOnly.md)**: min qualified cardinality 0 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isServicedBy](/concepts/fibo/LOAN/LoansGeneral/Loans/isServicedBy.md)**: min qualified cardinality 0 of type [Servicer](/concepts/fibo/LOAN/LoansGeneral/Loans/Servicer.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [LenderLienPosition](/concepts/fibo/LOAN/LoansGeneral/Loans/LenderLienPosition.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [LoanMarketCategory](/concepts/fibo/LOAN/LoansSpecific/LoanProducts/LoanMarketCategory.md)

## Annotations

- **label**: loan
- **definition**: debt instrument whereby one party extends money or credit to another party (or parties) with the understanding that the borrowed money will be repaid according to the terms of the contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
