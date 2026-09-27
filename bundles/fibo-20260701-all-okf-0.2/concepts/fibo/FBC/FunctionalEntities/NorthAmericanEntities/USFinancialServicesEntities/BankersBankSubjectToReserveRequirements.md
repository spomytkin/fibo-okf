---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bankers' bank subject to reserve requirements
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bankers' bank whose activities are limited by specific requirements of the Federal Reserve
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/nicpubweb/Content/DataDownload/NPW%20Data%20Dictionary.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/isSubjectToReserveRequirements
    value: 'true'
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BankersBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BankersBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BankersBankSubjectToReserveRequirements
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: bankers' bank subject to reserve requirements
type: Ontology Class
---

# bankers' bank subject to reserve requirements

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BankersBankSubjectToReserveRequirements>

## Definition

bankers' bank whose activities are limited by specific requirements of the Federal Reserve

## Relationships

- **Subclass of**: [BankersBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BankersBank.md)

## Constraints

- **[isSubjectToReserveRequirements](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/isSubjectToReserveRequirements.md)**: has value value `true`

## Annotations

- **label**: bankers' bank subject to reserve requirements
- **definition**: bankers' bank whose activities are limited by specific requirements of the Federal Reserve
- **adaptedFrom**: https://www.ffiec.gov/nicpubweb/Content/DataDownload/NPW%20Data%20Dictionary.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
