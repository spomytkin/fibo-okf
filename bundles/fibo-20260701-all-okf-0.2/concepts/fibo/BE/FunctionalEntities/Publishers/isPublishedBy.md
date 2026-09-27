---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is published by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the independent party (i.e., the individual or organization) that disseminates the material
  domain:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publication
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/isPublishedBy
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: is published by
type: Ontology Property
---

# is published by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/isPublishedBy>

## Definition

identifies the independent party (i.e., the individual or organization) that disseminates the material

## Relationships

- **Domain**: [Publication](/concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md)
- **Range**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Subproperty of**: [hasParty](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasParty>)

## Annotations

- **label**: is published by
- **definition**: identifies the independent party (i.e., the individual or organization) that disseminates the material

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
