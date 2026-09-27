---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: LEI registered entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a legal person that has registered for and is identified by a legal entity identifier
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the GLEIF data includes multiple LEIs for some entities due to corporate actions or other situations.
      The duplicates are typically archived after some period of time, but in order to reflect the reality in the data, the
      restriction is modeled as someValuesFrom rather than exactly 1 LEI for a given entity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LEIRegisteredEntity
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: LEI registered entity
type: Ontology Class
---

# LEI registered entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LEIRegisteredEntity>

## Definition

a legal person that has registered for and is identified by a legal entity identifier

## Relationships

- **Subclass of**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Constraints

- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: some values from of type [LegalEntityIdentifier](/concepts/fibo/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)

## Annotations

- **label**: LEI registered entity
- **definition**: a legal person that has registered for and is identified by a legal entity identifier
- **explanatoryNote**: Note that the GLEIF data includes multiple LEIs for some entities due to corporate actions or other situations. The duplicates are typically archived after some period of time, but in order to reflect the reality in the data, the restriction is modeled as someValuesFrom rather than exactly 1 LEI for a given entity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
