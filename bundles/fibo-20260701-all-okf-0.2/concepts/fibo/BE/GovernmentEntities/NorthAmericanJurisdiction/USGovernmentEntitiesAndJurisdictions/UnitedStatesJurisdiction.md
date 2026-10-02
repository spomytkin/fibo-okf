---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: United States jurisdiction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual representing the federal jurisdiction of the United States of America
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://en.wikipedia.org/wiki/Federal_jurisdiction_(United_States)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.uscourts.gov/about-federal-courts
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The United States of America is a federal republic governed by the U.S. Constitution containing fifty states and
      a federal district which elect the president, and having other territories and possessions in its national jurisdiction.
      This government is known as the Union, the United States, or the federal government. Federal jurisdiction refers to
      the legal scope of the government's powers. Under the Constitution and various treaties, the legal jurisdiction of the
      United States includes territories and territorial waters.
  defined_by:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesGovernment.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/isJurisdictionOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesGovernment
  - predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasReach
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.uscourts.gov/about-federal-courts
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
sources:
- id: fibo-source-42205fd066
  resource: references/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.rdf
  sha256: 42205fd0664c2535036cff2d6c5bfbcf9a6ce4ad4cbae0af6910c63eac9f6bda
  title: FIBO source BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.rdf
title: United States jurisdiction
type: Ontology Individual
---

# United States jurisdiction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction>

## Definition

individual representing the federal jurisdiction of the United States of America

## Relationships

- **Defined by**: [USGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [UnitedStatesGovernment](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesGovernment.md)
- **See also**: [about-federal-courts](<http://www.uscourts.gov/about-federal-courts>)

## Annotations

- **label**: United States jurisdiction
- **definition**: individual representing the federal jurisdiction of the United States of America
- **adaptedFrom**: http://en.wikipedia.org/wiki/Federal_jurisdiction_(United_States)
- **adaptedFrom**: http://www.uscourts.gov/about-federal-courts
- **explanatoryNote**: The United States of America is a federal republic governed by the U.S. Constitution containing fifty states and a federal district which elect the president, and having other territories and possessions in its national jurisdiction. This government is known as the Union, the United States, or the federal government. Federal jurisdiction refers to the legal scope of the government's powers. Under the Constitution and various treaties, the legal jurisdiction of the United States includes territories and territorial waters.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
