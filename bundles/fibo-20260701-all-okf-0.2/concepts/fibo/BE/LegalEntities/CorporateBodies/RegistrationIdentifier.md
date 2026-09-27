---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registration identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier that is officially allocated to an organization at the time of registration, typically in a jurisdiction
      in which said organization is organized or registered and used in that jurisdiction to identify the organization
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: In some jurisdictions, such as the State of California, registration identifiers are issued to corporations, including
      non-profit corporations, limited liability companies, certain partnerships, and foreign corporations doing business
      in California. The same or a very similar process is used for registration of corporations across the US.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A registration identifier may be required for official communications and is publicly available. The relationship
      to the jurisdiction in which the organization is organized or registered is typically required, but is optional here
      to cover cases where jurisdictions may overlap or are not as clearly defined.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifierScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifier
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: registration identifier
type: Ontology Class
---

# registration identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifier>

## Definition

identifier that is officially allocated to an organization at the time of registration, typically in a jurisdiction in which said organization is organized or registered and used in that jurisdiction to identify the organization

## Relationships

- **Subclass of**: [OrganizationIdentifier](<https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier>)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [RegistrationIdentifierScheme](/concepts/fibo/BE/LegalEntities/CorporateBodies/RegistrationIdentifierScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)
- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: min qualified cardinality 0 of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: registration identifier
- **definition**: identifier that is officially allocated to an organization at the time of registration, typically in a jurisdiction in which said organization is organized or registered and used in that jurisdiction to identify the organization
- **scopeNote**: In some jurisdictions, such as the State of California, registration identifiers are issued to corporations, including non-profit corporations, limited liability companies, certain partnerships, and foreign corporations doing business in California. The same or a very similar process is used for registration of corporations across the US.
- **explanatoryNote**: A registration identifier may be required for official communications and is publicly available. The relationship to the jurisdiction in which the organization is organized or registered is typically required, but is optional here to cover cases where jurisdictions may overlap or are not as clearly defined.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
