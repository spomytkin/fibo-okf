---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: blacklisted
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether or not the strategy in framed so as to include the referenced business entity as being blacklisted. If
      yes, the strategy prevents investment in securities issued by that organization.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/OrganizationStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/OrganizationStrategy
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/blacklisted
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: blacklisted
type: Ontology Property
---

# blacklisted

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/blacklisted>

## Definition

Whether or not the strategy in framed so as to include the referenced business entity as being blacklisted. If yes, the strategy prevents investment in securities issued by that organization.

## Relationships

- **Domain**: [OrganizationStrategy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/OrganizationStrategy.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): blacklisted
- **definition** (en): Whether or not the strategy in framed so as to include the referenced business entity as being blacklisted. If yes, the strategy prevents investment in securities issued by that organization.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
