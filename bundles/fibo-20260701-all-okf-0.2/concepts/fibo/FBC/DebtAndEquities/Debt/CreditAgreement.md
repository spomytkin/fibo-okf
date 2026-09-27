---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual agreement in which a debtor receives something of value and typically agrees to repay the creditor
      by some date in the future, in some form (e.g., cash, securities, etc.), generally with interest
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialExchangeDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasMaturityDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasCorrespondingAccount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Creditor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debtor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/UseOfProceedsProvision
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DebtTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: credit agreement
type: Ontology Class
---

# credit agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement>

## Definition

contractual agreement in which a debtor receives something of value and typically agrees to repay the creditor by some date in the future, in some form (e.g., cash, securities, etc.), generally with interest

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[hasInitialExchangeDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInitialExchangeDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasMaturityDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasMaturityDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: min qualified cardinality 0 of type [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)
- **[hasCorrespondingAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasCorrespondingAccount.md)**: min qualified cardinality 0 of type [LoanOrCreditAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md)
- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: min qualified cardinality 0 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [Creditor](/concepts/fibo/FBC/DebtAndEquities/Debt/Creditor.md)
- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [Debtor](/concepts/fibo/FBC/DebtAndEquities/Debt/Debtor.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: min qualified cardinality 0 of type [UseOfProceedsProvision](/concepts/fibo/FND/Agreements/Contracts/UseOfProceedsProvision.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [DebtTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/DebtTerms.md)

## Annotations

- **label**: credit agreement
- **definition**: contractual agreement in which a debtor receives something of value and typically agrees to repay the creditor by some date in the future, in some form (e.g., cash, securities, etc.), generally with interest

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
