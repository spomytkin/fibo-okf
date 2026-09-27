---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Federal Reserve district
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a region of the US identifying the jurisdiction of a Federal Reserve Bank, numbered and named for the city in which
      that reserve bank is located
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://federalreserve.gov/otherfrb.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The Federal Reserve officially identifies Districts by number and Reserve Bank city. In the 12th District, the
      Seattle Branch serves Alaska, and the San Francisco Bank serves Hawaii. The System serves commonwealths and territories
      as follows: the New York Bank serves the Commonwealth of Puerto Rico and the U.S. Virgin Islands; the San Francisco
      Bank serves American Samoa, Guam, and the Commonwealth of the Northern Mariana Islands. The Board of Governors revised
      the branch boundaries of the System in February 1996.'
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveDistrict
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Federal Reserve district
type: Ontology Class
---

# Federal Reserve district

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveDistrict>

## Definition

a region of the US identifying the jurisdiction of a Federal Reserve Bank, numbered and named for the city in which that reserve bank is located

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Subclass of**: [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: Federal Reserve district
- **definition**: a region of the US identifying the jurisdiction of a Federal Reserve Bank, numbered and named for the city in which that reserve bank is located
- **adaptedFrom**: http://federalreserve.gov/otherfrb.htm
- **explanatoryNote**: The Federal Reserve officially identifies Districts by number and Reserve Bank city. In the 12th District, the Seattle Branch serves Alaska, and the San Francisco Bank serves Hawaii. The System serves commonwealths and territories as follows: the New York Bank serves the Commonwealth of Puerto Rico and the U.S. Virgin Islands; the San Francisco Bank serves American Samoa, Guam, and the Commonwealth of the Northern Mariana Islands. The Board of Governors revised the branch boundaries of the System in February 1996.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
