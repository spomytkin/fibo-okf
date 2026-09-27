---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: state government entity or agency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal organization that is an independent agency, instrumentality or other permanent or semi-permanent organization
      in the machinery of government of any one of the states or territories of the United States
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction
    value: N408714e075ce4cafa73cffa66eadbd94
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/StateGovernmentEntity
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: state government entity or agency
type: Ontology Class
---

# state government entity or agency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/StateGovernmentEntity>

## Definition

formal organization that is an independent agency, instrumentality or other permanent or semi-permanent organization in the machinery of government of any one of the states or territories of the United States

## Relationships

- **Subclass of**: [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)

## Constraints

- **[hasJurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction>)**: some values from value `N408714e075ce4cafa73cffa66eadbd94`

## Annotations

- **label**: state government entity or agency
- **definition**: formal organization that is an independent agency, instrumentality or other permanent or semi-permanent organization in the machinery of government of any one of the states or territories of the United States

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
