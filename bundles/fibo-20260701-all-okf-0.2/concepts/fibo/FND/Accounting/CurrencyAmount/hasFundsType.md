---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has funds type
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the type of funds, such as next day for US funds
  domain:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Funds.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Funds
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasFundsType
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: has funds type
type: Ontology Property
---

# has funds type

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasFundsType>

## Definition

indicates the type of funds, such as next day for US funds

## Relationships

- **Domain**: [Funds](/concepts/fibo/FND/Accounting/CurrencyAmount/Funds.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)
- **Subproperty of**: [hasTextValue](<https://www.omg.org/spec/Commons/TextDatatype/hasTextValue>)

## Annotations

- **label**: has funds type
- **definition**: indicates the type of funds, such as next day for US funds

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
