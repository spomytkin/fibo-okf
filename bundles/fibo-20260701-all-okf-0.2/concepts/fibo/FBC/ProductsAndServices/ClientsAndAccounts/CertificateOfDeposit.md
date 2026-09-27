---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: certificate of deposit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cash instrument associated with a time deposit account that cannot be withdrawn for a certain period of time (term)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CD
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: When the term is over it can be withdrawn or it can be held for another term. The longer the term the better the
      yield on the money.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasNominalValue
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractDuration
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CashInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CashInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CertificateOfDeposit
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: certificate of deposit
type: Ontology Class
---

# certificate of deposit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CertificateOfDeposit>

## Definition

cash instrument associated with a time deposit account that cannot be withdrawn for a certain period of time (term)

## Relationships

- **Subclass of**: [CashInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CashInstrument.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: exact qualified cardinality 1 of type [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **[hasNominalValue](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasNominalValue.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasContractDuration](/concepts/fibo/FND/Agreements/Contracts/hasContractDuration.md)**: exact qualified cardinality 1 of type [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)

## Annotations

- **label** (en): certificate of deposit
- **definition** (en): cash instrument associated with a time deposit account that cannot be withdrawn for a certain period of time (term)
- **abbreviation**: CD
- **explanatoryNote**: When the term is over it can be withdrawn or it can be held for another term. The longer the term the better the yield on the money.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
