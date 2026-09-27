---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: State of Virginia jurisdiction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual representing the overall jurisdiction for the US State of Virginia, i.e., that of the Virginia Supreme
      Court and Judiciary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Commonwealth of Virginia jurisdiction
  defined_by:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfVirginiaGovernment.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/isJurisdictionOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfVirginiaGovernment
  - predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasReach
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Virginia
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.courts.state.va.us/courts/home.html
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfVirginiaJurisdiction
sources:
- id: fibo-source-42205fd066
  resource: references/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.rdf
  sha256: 42205fd0664c2535036cff2d6c5bfbcf9a6ce4ad4cbae0af6910c63eac9f6bda
  title: FIBO source BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.rdf
title: State of Virginia jurisdiction
type: Ontology Individual
---

# State of Virginia jurisdiction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfVirginiaJurisdiction>

## Definition

individual representing the overall jurisdiction for the US State of Virginia, i.e., that of the Virginia Supreme Court and Judiciary

## Relationships

- **Defined by**: [USGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [Virginia](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Virginia>)
- **Related to**: [StateOfVirginiaGovernment](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfVirginiaGovernment.md)
- **See also**: [home.html](<http://www.courts.state.va.us/courts/home.html>)

## Annotations

- **label**: State of Virginia jurisdiction
- **definition**: individual representing the overall jurisdiction for the US State of Virginia, i.e., that of the Virginia Supreme Court and Judiciary
- **synonym**: Commonwealth of Virginia jurisdiction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
