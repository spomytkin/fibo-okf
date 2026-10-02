---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business identifier code scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: scheme that specifies the elements of a unique business identifier code (BIC) scheme to identify financial and
      non-financial institutions used to facilitate automated processing of information for financial services
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 9362:2014 Banking -- Banking telecommunication messages -- Business identifier code (BIC)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso.org/standard/60390.html
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationIdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: business identifier code scheme
type: Ontology Class
---

# business identifier code scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme>

## Definition

scheme that specifies the elements of a unique business identifier code (BIC) scheme to identify financial and non-financial institutions used to facilitate automated processing of information for financial services

## Relationships

- **Subclass of**: [CodeSet](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet>)
- **Subclass of**: [OrganizationIdentificationScheme](<https://www.omg.org/spec/Commons/Organizations/OrganizationIdentificationScheme>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [BusinessIdentifierCode](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode.md)

## Annotations

- **label**: business identifier code scheme
- **definition**: scheme that specifies the elements of a unique business identifier code (BIC) scheme to identify financial and non-financial institutions used to facilitate automated processing of information for financial services
- **adaptedFrom**: ISO 9362:2014 Banking -- Banking telecommunication messages -- Business identifier code (BIC)
- **adaptedFrom**: https://www.iso.org/standard/60390.html

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
