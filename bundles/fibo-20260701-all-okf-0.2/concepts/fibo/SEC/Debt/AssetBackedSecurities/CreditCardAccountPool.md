---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit card account pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: pool of credit card receivables associated with designated accounts
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Federal Deposit Insurance Corporation (FDIC) Credit Card Securitization Manual, available at https://www.fdic.gov/regulations/examinations/credit_card_securitization/ch2.html
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a credit card securitization transaction only the receivables are sold, not the accounts that generate the receivables.
      The financial institution retains legal ownership of the credit card accounts and can continue to change the terms on
      the accounts. Accounts corresponding to securitized loans are typically referred to as the designated accounts (or sometimes
      trust accounts). The initial outstanding balances on the designated accounts are sold to the trust as are the rights
      to any new charges on the designated accounts. Subsequently, as cardholder purchase activity generates more receivables
      on the designated accounts, these new receivables are purchased by the trust from the originating institution/seller/transferor.
      The trust uses the monthly principal payments received from the cardholders to acquire these new charges or receivables.
      When the securitization is initially set up, the originating institution/seller adds sufficient receivables to support
      the principal balance of the certificates plus an additional amount (seller's interest) that serves to absorb fluctuations
      in the outstanding balance of the receivables. The originating institution/seller will make subsequent additions to
      the trust in order to keep the seller's interest at the required level.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAccount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/CreditCardAccountPool
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: credit card account pool
type: Ontology Class
---

# credit card account pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/CreditCardAccountPool>

## Definition

pool of credit card receivables associated with designated accounts

## Relationships

- **Subclass of**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Constraints

- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: some values from of type [CreditCardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAccount.md)

## Annotations

- **label** (en): credit card account pool
- **definition** (en): pool of credit card receivables associated with designated accounts
- **adaptedFrom** (en): Federal Deposit Insurance Corporation (FDIC) Credit Card Securitization Manual, available at https://www.fdic.gov/regulations/examinations/credit_card_securitization/ch2.html
- **explanatoryNote** (en): In a credit card securitization transaction only the receivables are sold, not the accounts that generate the receivables. The financial institution retains legal ownership of the credit card accounts and can continue to change the terms on the accounts. Accounts corresponding to securitized loans are typically referred to as the designated accounts (or sometimes trust accounts). The initial outstanding balances on the designated accounts are sold to the trust as are the rights to any new charges on the designated accounts. Subsequently, as cardholder purchase activity generates more receivables on the designated accounts, these new receivables are purchased by the trust from the originating institution/seller/transferor. The trust uses the monthly principal payments received from the cardholders to acquire these new charges or receivables. When the securitization is initially set up, the originating institution/seller adds sufficient receivables to support the principal balance of the certificates plus an additional amount (seller's interest) that serves to absorb fluctuations in the outstanding balance of the receivables. The originating institution/seller will make subsequent additions to the trust in order to keep the seller's interest at the required level.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
