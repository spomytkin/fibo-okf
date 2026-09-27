---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has originating service provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something, typically a loan contract, to the service provider responsible for originated the loan
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically this will be a bank, mortgage broker, investment bank, or other similar party.
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasOriginatingServiceProvider
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: has originating service provider
type: Ontology Property
---

# has originating service provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasOriginatingServiceProvider>

## Definition

relates something, typically a loan contract, to the service provider responsible for originated the loan

## Relationships

- **Subproperty of**: [hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)

## Annotations

- **label**: has originating service provider
- **definition**: relates something, typically a loan contract, to the service provider responsible for originated the loan
- **explanatoryNote**: Typically this will be a bank, mortgage broker, investment bank, or other similar party.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
