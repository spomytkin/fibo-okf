---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has publisher
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the party in the role of issuing the information
  domain:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publication
  inverse_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/publishes.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/publishes
  range:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/manifests
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: has publisher
type: Ontology Property
---

# has publisher

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher>

## Definition

indicates the party in the role of issuing the information

## Relationships

- **Domain**: [Publication](/concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md)
- **Inverse of**: [publishes](/concepts/fibo/BE/FunctionalEntities/Publishers/publishes.md)
- **Range**: [Publisher](/concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md)
- **Subproperty of**: [hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)
- **Subproperty of**: [manifests](<https://www.omg.org/spec/Commons/RolesAndCompositions/manifests>)

## Annotations

- **label**: has publisher
- **definition**: indicates the party in the role of issuing the information

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
