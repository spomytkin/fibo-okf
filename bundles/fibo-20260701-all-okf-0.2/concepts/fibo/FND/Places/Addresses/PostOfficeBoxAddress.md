---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: post office box address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical address used to deliver communications to a designated container at a local post office or the local equivalent
      for the jurisdiction, where mail is held until the recipient collects it, rather than to a given house, building, or
      other location
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostOfficeBox
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostOfficeBoxAddress
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: post office box address
type: Ontology Class
---

# post office box address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostOfficeBoxAddress>

## Definition

physical address used to deliver communications to a designated container at a local post office or the local equivalent for the jurisdiction, where mail is held until the recipient collects it, rather than to a given house, building, or other location

## Relationships

- **Subclass of**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [PostOfficeBox](/concepts/fibo/FND/Places/Addresses/PostOfficeBox.md)

## Annotations

- **label**: post office box address
- **definition**: physical address used to deliver communications to a designated container at a local post office or the local equivalent for the jurisdiction, where mail is held until the recipient collects it, rather than to a given house, building, or other location

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
