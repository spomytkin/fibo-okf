---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: supplemental address component
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: address component that provides additional information that is important to ensuring proper delivery of communications
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Supplemental components include post office box information, rural route and highway contract route information,
      private mailboxes, and so forth, that are not part of a conventional street address.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressDesignator
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressUnit
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/AddressComponent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressComponent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressComponent
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: supplemental address component
type: Ontology Class
---

# supplemental address component

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressComponent>

## Definition

address component that provides additional information that is important to ensuring proper delivery of communications

## Relationships

- **Subclass of**: [AddressComponent](/concepts/fibo/FND/Places/Addresses/AddressComponent.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [SupplementalAddressDesignator](/concepts/fibo/FND/Places/Addresses/SupplementalAddressDesignator.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [SupplementalAddressUnit](/concepts/fibo/FND/Places/Addresses/SupplementalAddressUnit.md)
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)

## Annotations

- **label**: supplemental address component
- **definition**: address component that provides additional information that is important to ensuring proper delivery of communications
- **explanatoryNote**: Supplemental components include post office box information, rural route and highway contract route information, private mailboxes, and so forth, that are not part of a conventional street address.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
