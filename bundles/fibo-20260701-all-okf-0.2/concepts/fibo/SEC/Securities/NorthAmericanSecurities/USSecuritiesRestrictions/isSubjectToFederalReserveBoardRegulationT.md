---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is subject to Federal Reserve Board Regulation T
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether a given cash or margin account is subject to Federal Reserve Board (FRB) margin requirements
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Federal Reserve Board (FRB) Regulation T governs the extension of credit by securities brokers and dealers in the
      United States. Its best-known function is the control of margin requirements for stocks bought on margin. Regulation
      T gives an investor a maximum of four business days to pay for securities purchased in a cash or margin account. If
      payment due exceeds $1,000 and is not received by the end of this time period, the broker-dealer must either liquidate
      the position or apply for and receive an extensionfrom its designated examining authority, such as FINRA.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Note that this property applies to the account, which may be a ledger account.
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.finra.org/filing-reporting/regulation-t-filings
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/isSubjectToFederalReserveBoardRegulationT
sources:
- id: fibo-source-91c51c4810
  resource: references/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
  sha256: 91c51c4810cfe6c5acc0aaf99de529357298d47f01cfe4f5eee4962f40f5be33
  title: FIBO source SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
title: is subject to Federal Reserve Board Regulation T
type: Ontology Property
---

# is subject to Federal Reserve Board Regulation T

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/isSubjectToFederalReserveBoardRegulationT>

## Definition

indicates whether a given cash or margin account is subject to Federal Reserve Board (FRB) margin requirements

## Relationships

- **Domain**: [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **See also**: [regulation-t-filings](<https://www.finra.org/filing-reporting/regulation-t-filings>)

## Annotations

- **label**: is subject to Federal Reserve Board Regulation T
- **definition**: indicates whether a given cash or margin account is subject to Federal Reserve Board (FRB) margin requirements
- **explanatoryNote**: Federal Reserve Board (FRB) Regulation T governs the extension of credit by securities brokers and dealers in the United States. Its best-known function is the control of margin requirements for stocks bought on margin. Regulation T gives an investor a maximum of four business days to pay for securities purchased in a cash or margin account. If payment due exceeds $1,000 and is not received by the end of this time period, the broker-dealer must either liquidate the position or apply for and receive an extensionfrom its designated examining authority, such as FINRA.
- **usageNote**: Note that this property applies to the account, which may be a ledger account.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
