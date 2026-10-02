---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: monetary price
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: price that that is expressed as a monetary amount
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: As the consideration given in exchange for transfer of ownership, price forms the essential basis of commercial
      transactions. It may be fixed by a contract, left to be determined by an agreed upon formula at a future date, or discovered
      or negotiated during the course of dealings between the parties involved. In commerce, price is determined by what (1)
      a buyer is willing to pay, (2) a seller is willing to accept, and (3) the competition is allowing to be charged.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Price.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Price
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: monetary price
type: Ontology Class
---

# monetary price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice>

## Definition

price that that is expressed as a monetary amount

## Relationships

- **Subclass of**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subclass of**: [Price](/concepts/fibo/FND/Accounting/CurrencyAmount/Price.md)

## Annotations

- **label**: monetary price
- **definition**: price that that is expressed as a monetary amount
- **explanatoryNote**: As the consideration given in exchange for transfer of ownership, price forms the essential basis of commercial transactions. It may be fixed by a contract, left to be determined by an agreed upon formula at a future date, or discovered or negotiated during the course of dealings between the parties involved. In commerce, price is determined by what (1) a buyer is willing to pay, (2) a seller is willing to accept, and (3) the competition is allowing to be charged.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
