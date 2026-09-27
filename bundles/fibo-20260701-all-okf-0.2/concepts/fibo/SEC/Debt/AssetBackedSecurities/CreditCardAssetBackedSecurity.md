---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit card asset-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset-backed security based on credit card receivables
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Federal Deposit Insurance Corporation (FDIC) Credit Card Securitization Manual, available at https://www.fdic.gov/regulations/examinations/credit_card_securitization/ch2.html
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Credit card securitizations currently represent the primary funding vehicle for unsecured revolving consumer credit.
      Similar to mortgage and other asset securitizations, the financial institution that originates the credit card receivables
      sells a group of these receivables to a trust. The trust then creates and sells certificates backed by the credit card
      receivables to investors, which are predominately institutional investors. Very few credit card ABS are marketed to
      retail customers, primarily due to the complex nature of the transactions and the need to continually monitor various
      performance indices on the underlying receivables. The underlying credit card receivables generate income to support
      the interest payments on the certificates.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/CreditCardAccountPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/CreditCardAssetBackedSecurity
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: credit card asset-backed security
type: Ontology Class
---

# credit card asset-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/CreditCardAssetBackedSecurity>

## Definition

asset-backed security based on credit card receivables

## Relationships

- **Subclass of**: [AssetBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [CreditCardAccountPool](/concepts/fibo/SEC/Debt/AssetBackedSecurities/CreditCardAccountPool.md)

## Annotations

- **label** (en): credit card asset-backed security
- **definition** (en): asset-backed security based on credit card receivables
- **adaptedFrom** (en): Federal Deposit Insurance Corporation (FDIC) Credit Card Securitization Manual, available at https://www.fdic.gov/regulations/examinations/credit_card_securitization/ch2.html
- **explanatoryNote** (en): Credit card securitizations currently represent the primary funding vehicle for unsecured revolving consumer credit. Similar to mortgage and other asset securitizations, the financial institution that originates the credit card receivables sells a group of these receivables to a trust. The trust then creates and sells certificates backed by the credit card receivables to investors, which are predominately institutional investors. Very few credit card ABS are marketed to retail customers, primarily due to the complex nature of the transactions and the need to continually monitor various performance indices on the underlying receivables. The underlying credit card receivables generate income to support the interest payments on the certificates.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
