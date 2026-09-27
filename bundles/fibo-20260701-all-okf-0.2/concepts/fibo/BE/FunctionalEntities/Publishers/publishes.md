---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: publishes
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: prepares and issues material for public consumption
  domain:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
  range:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publication
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/isManifestedIn
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/publishes
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: publishes
type: Ontology Property
---

# publishes

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/publishes>

## Definition

prepares and issues material for public consumption

## Relationships

- **Domain**: [Publisher](/concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md)
- **Range**: [Publication](/concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md)
- **Subproperty of**: [isManifestedIn](<https://www.omg.org/spec/Commons/RolesAndCompositions/isManifestedIn>)

## Annotations

- **label**: publishes
- **definition**: prepares and issues material for public consumption

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
