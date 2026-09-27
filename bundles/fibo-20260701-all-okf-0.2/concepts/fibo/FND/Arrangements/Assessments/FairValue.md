---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fair value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: price that would be received to sell an asset, or paid to transfer a liability, in an orderly transaction between
      market participants at the measurement date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO/TS 55010:2024(en), Asset management - Guidance on the alignment of financial and non-financial functions in
      asset management
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://en.wikipedia.org/wiki/Fair_value
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  - concept: /concepts/fibo/FND/Arrangements/Assessments/QuantitativeValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/QuantitativeValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/FairValue
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: fair value
type: Ontology Class
---

# fair value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/FairValue>

## Definition

price that would be received to sell an asset, or paid to transfer a liability, in an orderly transaction between market participants at the measurement date

## Relationships

- **See also**: [Fair_value](<https://en.wikipedia.org/wiki/Fair_value>)
- **Subclass of**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subclass of**: [QuantitativeValue](/concepts/fibo/FND/Arrangements/Assessments/QuantitativeValue.md)

## Annotations

- **label**: fair value
- **definition**: price that would be received to sell an asset, or paid to transfer a liability, in an orderly transaction between market participants at the measurement date
- **adaptedFrom**: ISO/TS 55010:2024(en), Asset management - Guidance on the alignment of financial and non-financial functions in asset management

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
