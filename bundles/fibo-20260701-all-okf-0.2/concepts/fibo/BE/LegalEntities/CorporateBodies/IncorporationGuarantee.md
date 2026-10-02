---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: incorporation guarantee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: guarantee that is part of the financial basis by which some legal entity is incorporated
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNotionalAmount
  - cardinality: 1
    kind: exact_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCore/Constitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Constitution
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/IncorporationGuarantee
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: incorporation guarantee
type: Ontology Class
---

# incorporation guarantee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/IncorporationGuarantee>

## Definition

guarantee that is part of the financial basis by which some legal entity is incorporated

## Relationships

- **Subclass of**: [Constitution](/concepts/fibo/FND/Law/LegalCore/Constitution.md)

## Constraints

- **[hasNotionalAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasNotionalAmount.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: exact cardinality 1

## Annotations

- **label**: incorporation guarantee
- **definition**: guarantee that is part of the financial basis by which some legal entity is incorporated

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
