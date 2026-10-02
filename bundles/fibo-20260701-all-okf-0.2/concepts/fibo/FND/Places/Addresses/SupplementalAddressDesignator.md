---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: supplemental address designator
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for supplemental address information, such as a highway contract route, rural route, building complex,
      shopping center, condominium complex, mail box, or other similar designation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressComponent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressDesignator
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: supplemental address designator
type: Ontology Class
---

# supplemental address designator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressDesignator>

## Definition

classifier for supplemental address information, such as a highway contract route, rural route, building complex, shopping center, condominium complex, mail box, or other similar designation

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [SupplementalAddressComponent](/concepts/fibo/FND/Places/Addresses/SupplementalAddressComponent.md)

## Annotations

- **label**: supplemental address designator
- **definition**: classifier for supplemental address information, such as a highway contract route, rural route, building complex, shopping center, condominium complex, mail box, or other similar designation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
