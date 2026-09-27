---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has numeric code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a numeric code to something, such as a currency or fund
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: In the case of currency codes, the numeric currency code is derived, where possible, from the United Nations Standard
      Country or Area Code. Additional codes to meet special requirements (as described in 5.1.3) and in respect of funds
      will be allocated as necessary from within the user-assigned range of codes 950 to 998. Funds codes are allocated in
      descending order commencing at 998.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: has numeric code
type: Ontology Property
---

# has numeric code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode>

## Definition

relates a numeric code to something, such as a currency or fund

## Relationships

- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)
- **Subproperty of**: [hasTextValue](<https://www.omg.org/spec/Commons/TextDatatype/hasTextValue>)

## Annotations

- **label**: has numeric code
- **definition**: relates a numeric code to something, such as a currency or fund
- **scopeNote**: In the case of currency codes, the numeric currency code is derived, where possible, from the United Nations Standard Country or Area Code. Additional codes to meet special requirements (as described in 5.1.3) and in respect of funds will be allocated as necessary from within the user-assigned range of codes 950 to 998. Funds codes are allocated in descending order commencing at 998.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
