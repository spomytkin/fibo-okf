---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has issued capital
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the aggregate value of all shares held by shareholders
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A corporation can, at any time, issue new shares up to the full amount of authorized share capital.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has subscribed capital
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has subscribed share capital
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasIssuedCapital
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: has issued capital
type: Ontology Property
---

# has issued capital

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasIssuedCapital>

## Definition

indicates the aggregate value of all shares held by shareholders

## Relationships

- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label**: has issued capital
- **definition**: indicates the aggregate value of all shares held by shareholders
- **explanatoryNote**: A corporation can, at any time, issue new shares up to the full amount of authorized share capital.
- **synonym**: has subscribed capital
- **synonym**: has subscribed share capital

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
