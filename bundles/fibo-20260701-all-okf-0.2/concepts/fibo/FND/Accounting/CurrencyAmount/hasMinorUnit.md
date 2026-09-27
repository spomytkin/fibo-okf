---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has minor unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a code for the minor unit of currency to the currency or fund
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: "Requirements sometimes arise for values to be expressed in terms of minor units of currency. When this occurs,\
      \ it is necessary to know the decimal relationship that exists between the currency concerned and its minor unit. \n\
      - 0 means that there is no minor unit for the currency; \n- 1, 2, and 3 signify a ratio of 10 to 1, 100 to 1 and 1000\
      \ to 1 respectively."
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: has minor unit
type: Ontology Property
---

# has minor unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit>

## Definition

relates a code for the minor unit of currency to the currency or fund

## Relationships

- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)
- **Subproperty of**: [hasTextValue](<https://www.omg.org/spec/Commons/TextDatatype/hasTextValue>)

## Annotations

- **label**: has minor unit
- **definition**: relates a code for the minor unit of currency to the currency or fund
- **scopeNote**: Requirements sometimes arise for values to be expressed in terms of minor units of currency. When this occurs, it is necessary to know the decimal relationship that exists between the currency concerned and its minor unit.  - 0 means that there is no minor unit for the currency;  - 1, 2, and 3 signify a ratio of 10 to 1, 100 to 1 and 1000 to 1 respectively.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
