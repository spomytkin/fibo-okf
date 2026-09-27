---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: situation in which some party holds the legal title to something (explicitly or implicitly) and has the right to
      transfer that title and/or possession
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Ownership is the right to possess, use, sell, donate or give as a gift any asset or property belonging to a person
      known as the 'owner'. An owner can be either a beneficial owner or a legal owner.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwnedAsset
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwningParty
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: ownership
type: Ontology Class
---

# ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership>

## Definition

situation in which some party holds the legal title to something (explicitly or implicitly) and has the right to transfer that title and/or possession

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[hasOwnedAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwnedAsset.md)**: some values from of type [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **[hasOwningParty](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwningParty.md)**: some values from of type [Owner](/concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md)

## Annotations

- **label** (en): ownership
- **definition**: situation in which some party holds the legal title to something (explicitly or implicitly) and has the right to transfer that title and/or possession
- **explanatoryNote**: Ownership is the right to possess, use, sell, donate or give as a gift any asset or property belonging to a person known as the 'owner'. An owner can be either a beneficial owner or a legal owner.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
