---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has spatial boundary
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a geographic region included in an environmental or sustainability assessment, which may cover a specific
      site, facility, region, or the global operations of a company or project
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Locations/GeographicRegion
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Locations/hasRegion
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/hasSpatialBoundary
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: has spatial boundary
type: Ontology Property
---

# has spatial boundary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/hasSpatialBoundary>

## Definition

specifies a geographic region included in an environmental or sustainability assessment, which may cover a specific site, facility, region, or the global operations of a company or project

## Relationships

- **Range**: [GeographicRegion](<https://www.omg.org/spec/Commons/Locations/GeographicRegion>)
- **Subproperty of**: [hasRegion](<https://www.omg.org/spec/Commons/Locations/hasRegion>)

## Annotations

- **label**: has spatial boundary
- **definition**: specifies a geographic region included in an environmental or sustainability assessment, which may cover a specific site, facility, region, or the global operations of a company or project

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
