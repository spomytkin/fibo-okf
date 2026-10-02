---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: association
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: not-for-profit organization that is owned by and acts on behalf of its members
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Associations include trade or business associations, industry sector-specific groups, and professional associations,
      among others. They also commonly include cooperative farms and markets.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/CooperativeSociety
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Association
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: association
type: Ontology Class
---

# association

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Association>

## Definition

not-for-profit organization that is owned by and acts on behalf of its members

## Relationships

- **Subclass of**: [NotForProfitOrganization](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md)

## Constraints

- **[playsRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole>)**: min qualified cardinality 0 of type [CooperativeSociety](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/CooperativeSociety.md)

## Annotations

- **label**: association
- **definition**: not-for-profit organization that is owned by and acts on behalf of its members
- **explanatoryNote**: Associations include trade or business associations, industry sector-specific groups, and professional associations, among others. They also commonly include cooperative farms and markets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
