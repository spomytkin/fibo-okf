---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: syndicate member
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: role of an individual or organization that is a member of an alliance set up to pool resources and share risk with
      respect to a large transaction
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: participating member
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: syndicate participant
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Ne58b0d135b8f4c36a462e782aae976f8
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/SyndicateMember
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: syndicate member
type: Ontology Class
---

# syndicate member

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/SyndicateMember>

## Definition

role of an individual or organization that is a member of an alliance set up to pool resources and share risk with respect to a large transaction

## Relationships

- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Ne58b0d135b8f4c36a462e782aae976f8`

## Annotations

- **label** (en): syndicate member
- **definition** (en): role of an individual or organization that is a member of an alliance set up to pool resources and share risk with respect to a large transaction
- **synonym** (en): participating member
- **synonym** (en): syndicate participant

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
