---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: secondary unit designator
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for a smaller structure or component within a larger facility, such as an apartment, office, mail stop,
      or other similar designation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that only certain secondary units require a secondary range, such as an apartment number, to complete a delivery
      point.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/requiresSecondaryUnitRange
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnitDesignator
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: secondary unit designator
type: Ontology Class
---

# secondary unit designator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnitDesignator>

## Definition

classifier for a smaller structure or component within a larger facility, such as an apartment, office, mail stop, or other similar designation

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[requiresSecondaryUnitRange](/concepts/fibo/FND/Places/Addresses/requiresSecondaryUnitRange.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: secondary unit designator
- **definition**: classifier for a smaller structure or component within a larger facility, such as an apartment, office, mail stop, or other similar designation
- **explanatoryNote**: Note that only certain secondary units require a secondary range, such as an apartment number, to complete a delivery point.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
