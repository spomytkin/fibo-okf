---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: region-specific identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: geographic region or subdivision identifier used internally by a country or other region
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/RegionSpecificIdentifier
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: region-specific identifier
type: Ontology Class
---

# region-specific identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/RegionSpecificIdentifier>

## Definition

geographic region or subdivision identifier used internally by a country or other region

## Relationships

- **Subclass of**: [GeographicRegionIdentifier](<https://www.omg.org/spec/Commons/Locations/GeographicRegionIdentifier>)

## Constraints

- **[isUsedBy](<https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy>)**: some values from of type [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)

## Annotations

- **label**: region-specific identifier
- **definition**: geographic region or subdivision identifier used internally by a country or other region

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
