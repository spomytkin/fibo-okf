---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has shares authorized
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the maximum number of shares that are permitted to be issued, as established by the board of directors
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An initial number of authorized shares is typically established at the time of incorporation, and is documented
      in articles of incorporation. The number of shares authorized may be extended from time to time by the board of directors
      as needed, and articles of incorporation and other legal documentation will be amended accordingly. It includes shares
      that are available, but not yet issued, for sale to generate capital, and shares available for distribution to insiders
      as part of their compensation packages.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasAmount
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasSharesAuthorized
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: has shares authorized
type: Ontology Property
---

# has shares authorized

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasSharesAuthorized>

## Definition

indicates the maximum number of shares that are permitted to be issued, as established by the board of directors

## Relationships

- **Range**: [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **Subproperty of**: [hasAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md)

## Annotations

- **label** (en): has shares authorized
- **definition** (en): indicates the maximum number of shares that are permitted to be issued, as established by the board of directors
- **explanatoryNote** (en): An initial number of authorized shares is typically established at the time of incorporation, and is documented in articles of incorporation. The number of shares authorized may be extended from time to time by the board of directors as needed, and articles of incorporation and other legal documentation will be amended accordingly. It includes shares that are available, but not yet issued, for sale to generate capital, and shares available for distribution to insiders as part of their compensation packages.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
