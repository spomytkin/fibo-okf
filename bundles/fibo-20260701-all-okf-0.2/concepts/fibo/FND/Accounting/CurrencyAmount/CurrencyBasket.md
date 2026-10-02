---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency basket
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: selected group of currencies, in which the weighted average is used as a measure of the value or the amount of
      an obligation
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: A currency basket functions as a benchmark for regional currency movements; its composition and weighting depends
      on its purpose.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Codes for the representation of currencies and funds, ISO 4217, Eighth edition, 2015-08-01, section 3.2
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/StructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyBasket
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: currency basket
type: Ontology Class
---

# currency basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CurrencyBasket>

## Definition

selected group of currencies, in which the weighted average is used as a measure of the value or the amount of an obligation

## Relationships

- **Subclass of**: [StructuredCollection](<https://www.omg.org/spec/Commons/Collections/StructuredCollection>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: currency basket
- **definition**: selected group of currencies, in which the weighted average is used as a measure of the value or the amount of an obligation
- **note**: A currency basket functions as a benchmark for regional currency movements; its composition and weighting depends on its purpose.
- **definitionOrigin**: Codes for the representation of currencies and funds, ISO 4217, Eighth edition, 2015-08-01, section 3.2

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
