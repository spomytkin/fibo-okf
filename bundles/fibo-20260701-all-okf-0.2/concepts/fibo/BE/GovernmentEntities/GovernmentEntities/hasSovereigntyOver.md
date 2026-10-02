---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has sovereignty over
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a polity to a geopolitical entity where the polity exercises dominion and authority of a political state
  domain:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/hasSovereigntyOver
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: has sovereignty over
type: Ontology Property
---

# has sovereignty over

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/hasSovereigntyOver>

## Definition

relates a polity to a geopolitical entity where the polity exercises dominion and authority of a political state

## Relationships

- **Domain**: [Polity](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md)
- **Range**: [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)
- **Subproperty of**: [governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)

## Annotations

- **label**: has sovereignty over
- **definition**: relates a polity to a geopolitical entity where the polity exercises dominion and authority of a political state

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
