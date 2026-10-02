---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registered charity program number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: concatenation of an entity's business number, the 'RR' abbreviation and a 4-digit subaccount number used for registered
      charity contribution
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 000000000RR0001
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.canada.ca/en/revenue-agency/services/charities-giving/charities/operating-a-registered-charity/registration-number.html
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An organization may have more than one registered charity account through its subunits, this is handled through
      additional 4-digit subaccount numbers. This is used as both an account and an identifier for the registration.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/RegisteredCharityProgramNumberIdentifierScheme
  - kind: has_value
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/RegisteredCharityProgramNumber
sources:
- id: fibo-source-3a86c5f7dd
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
  sha256: 3a86c5f7dd7acfa3d8ca47686faffd64ac5f85eae9e50730e1337823edbfcda4
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
title: registered charity program number
type: Ontology Class
---

# registered charity program number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/RegisteredCharityProgramNumber>

## Definition

concatenation of an entity's business number, the 'RR' abbreviation and a 4-digit subaccount number used for registered charity contribution

## Relationships

- **Subclass of**: [BusinessNumber](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber.md)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/RegisteredCharityProgramNumberIdentifierScheme`
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction`
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: min qualified cardinality 0 of type [LedgerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md)

## Annotations

- **label**: registered charity program number
- **definition**: concatenation of an entity's business number, the 'RR' abbreviation and a 4-digit subaccount number used for registered charity contribution
- **example**: 000000000RR0001
- **adaptedFrom**: https://www.canada.ca/en/revenue-agency/services/charities-giving/charities/operating-a-registered-charity/registration-number.html
- **explanatoryNote**: An organization may have more than one registered charity account through its subunits, this is handled through additional 4-digit subaccount numbers. This is used as both an account and an identifier for the registration.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
