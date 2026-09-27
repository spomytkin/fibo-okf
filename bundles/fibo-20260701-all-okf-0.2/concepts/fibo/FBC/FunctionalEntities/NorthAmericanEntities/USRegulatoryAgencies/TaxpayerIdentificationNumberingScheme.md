---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: taxpayer identification numbering scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: tax identification scheme used in the United States
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.irs.gov/individuals/international-taxpayers/taxpayer-identification-numbers-tin
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
  subclass_of:
  - concept: /concepts/fibo/FND/Parties/Parties/TaxIdentificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumberingScheme
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: taxpayer identification numbering scheme
type: Ontology Class
---

# taxpayer identification numbering scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumberingScheme>

## Definition

tax identification scheme used in the United States

## Relationships

- **Subclass of**: [TaxIdentificationScheme](/concepts/fibo/FND/Parties/Parties/TaxIdentificationScheme.md)

## Constraints

- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction`

## Annotations

- **label**: taxpayer identification numbering scheme
- **definition**: tax identification scheme used in the United States
- **adaptedFrom**: https://www.irs.gov/individuals/international-taxpayers/taxpayer-identification-numbers-tin

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
