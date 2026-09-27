---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is price for
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a price to something it provides a value for
  domain:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Price.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Price
  inverse_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/refersTo
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/isPriceFor
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: is price for
type: Ontology Property
---

# is price for

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/isPriceFor>

## Definition

links a price to something it provides a value for

## Relationships

- **Domain**: [Price](/concepts/fibo/FND/Accounting/CurrencyAmount/Price.md)
- **Inverse of**: [hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)
- **Subproperty of**: [refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)

## Annotations

- **label**: is price for
- **definition**: links a price to something it provides a value for

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
