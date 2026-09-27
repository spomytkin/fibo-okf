---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is Federal Deposit Insurance Corporation insured
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the security is covered by Federal Deposit Insurance Corporation (FDIC) insurance
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: FDIC coverage extends to Certificates of Deposit (CDs) and Money Market Accounts (MMAs) held at FDIC-insured institutions
      up to $250,000 per account.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Note that this property applies to the account rather than to the associated instrument that, if it exists, exemplifies
      the account.
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.fdic.gov/resources/deposit-insurance/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/isFederalDepositInsuranceCorporationInsured
sources:
- id: fibo-source-91c51c4810
  resource: references/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
  sha256: 91c51c4810cfe6c5acc0aaf99de529357298d47f01cfe4f5eee4962f40f5be33
  title: FIBO source SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
title: is Federal Deposit Insurance Corporation insured
type: Ontology Property
---

# is Federal Deposit Insurance Corporation insured

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/isFederalDepositInsuranceCorporationInsured>

## Definition

indicates whether the security is covered by Federal Deposit Insurance Corporation (FDIC) insurance

## Relationships

- **Domain**: [NonTransactionDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **See also**: [deposit-insurance](<https://www.fdic.gov/resources/deposit-insurance/>)

## Annotations

- **label**: is Federal Deposit Insurance Corporation insured
- **definition**: indicates whether the security is covered by Federal Deposit Insurance Corporation (FDIC) insurance
- **explanatoryNote**: FDIC coverage extends to Certificates of Deposit (CDs) and Money Market Accounts (MMAs) held at FDIC-insured institutions up to $250,000 per account.
- **usageNote**: Note that this property applies to the account rather than to the associated instrument that, if it exists, exemplifies the account.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
