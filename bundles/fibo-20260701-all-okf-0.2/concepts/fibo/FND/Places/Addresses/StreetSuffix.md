---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: street suffix
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for a street or other delivery location, such as a dwelling located along a waterway
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The suffix may provide some insight into the size or length of the street, though not necessarily consistently.
      In some cities, the suffix differentiates the street from another in the same context, such as 19th Street vs. 19th
      Avenue in San Francisco.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/AddressComponent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressComponent
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetSuffix
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: street suffix
type: Ontology Class
---

# street suffix

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetSuffix>

## Definition

classifier for a street or other delivery location, such as a dwelling located along a waterway

## Relationships

- **Subclass of**: [AddressComponent](/concepts/fibo/FND/Places/Addresses/AddressComponent.md)
- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Annotations

- **label**: street suffix
- **definition**: classifier for a street or other delivery location, such as a dwelling located along a waterway
- **explanatoryNote**: The suffix may provide some insight into the size or length of the street, though not necessarily consistently. In some cities, the suffix differentiates the street from another in the same context, such as 19th Street vs. 19th Avenue in San Francisco.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
