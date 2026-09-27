---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has home exchange
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the exchange that is considered the primary market for a security; typically, but not always, in the
      country in which the security was originally issued
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: A security may have been originally listed on the Frankfurt exchange, but its current home is the London Stock
      Exchange, for example.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A primary market is one that issues new securities on an exchange for companies, governments, and other groups
      to obtain financing through debt-based or equity-based securities.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has primary market
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has primary trading market
  range:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasHomeExchange
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: has home exchange
type: Ontology Property
---

# has home exchange

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasHomeExchange>

## Definition

indicates the exchange that is considered the primary market for a security; typically, but not always, in the country in which the security was originally issued

## Relationships

- **Range**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)
- **Subproperty of**: [isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)

## Annotations

- **label**: has home exchange
- **definition**: indicates the exchange that is considered the primary market for a security; typically, but not always, in the country in which the security was originally issued
- **example**: A security may have been originally listed on the Frankfurt exchange, but its current home is the London Stock Exchange, for example.
- **explanatoryNote**: A primary market is one that issues new securities on an exchange for companies, governments, and other groups to obtain financing through debt-based or equity-based securities.
- **synonym**: has primary market
- **synonym**: has primary trading market

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
