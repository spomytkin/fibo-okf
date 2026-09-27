---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: affiliation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: situation in which a controlled party is affiliated with a controlling party for some period of time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/Control.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliation
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: affiliation
type: Ontology Class
---

# affiliation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliation>

## Definition

situation in which a controlled party is affiliated with a controlling party for some period of time

## Relationships

- **Subclass of**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)

## Constraints

- **[hasActor](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor>)**: some values from of type [ControllingAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md)
- **[hasUndergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer>)**: some values from of type [ControlledAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md)

## Annotations

- **label**: affiliation
- **definition**: situation in which a controlled party is affiliated with a controlling party for some period of time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
