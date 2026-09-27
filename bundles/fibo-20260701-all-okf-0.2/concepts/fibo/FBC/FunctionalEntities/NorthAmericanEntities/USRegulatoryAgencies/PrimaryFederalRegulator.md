---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: primary federal regulator
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: federal regulatory agency that is designated as the main agency responsible for oversight of a given institution
      for an institution
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.ffiec.gov/nicpubweb/nicweb/NicHome.aspx
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N8fd4bd7f5d7b4ae29d434776a7f96953
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/PrimaryFederalRegulator
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: primary federal regulator
type: Ontology Class
---

# primary federal regulator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/PrimaryFederalRegulator>

## Definition

federal regulatory agency that is designated as the main agency responsible for oversight of a given institution for an institution

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Subclass of**: [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N8fd4bd7f5d7b4ae29d434776a7f96953`

## Annotations

- **label**: primary federal regulator
- **definition**: federal regulatory agency that is designated as the main agency responsible for oversight of a given institution for an institution
- **adaptedFrom**: http://www.ffiec.gov/nicpubweb/nicweb/NicHome.aspx

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
