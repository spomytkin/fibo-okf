---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regulation identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an identifier associated with a regulation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Regulation
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentifier
sources:
- id: fibo-source-ef717d20cc
  resource: references/fibo/FBC/FunctionalEntities/RegulatoryAgencies.rdf
  sha256: ef717d20cc3804b8cc9643a625bf716211db11cc374a524b54dd5ce7e70bf1db
  title: FIBO source FBC/FunctionalEntities/RegulatoryAgencies.rdf
title: regulation identifier
type: Ontology Class
---

# regulation identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentifier>

## Definition

an identifier associated with a regulation

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: exact qualified cardinality 1 of type [RegulationIdentificationScheme](/concepts/fibo/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentificationScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Regulation](/concepts/fibo/FND/Law/LegalCapacity/Regulation.md)

## Annotations

- **label**: regulation identifier
- **definition**: an identifier associated with a regulation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
