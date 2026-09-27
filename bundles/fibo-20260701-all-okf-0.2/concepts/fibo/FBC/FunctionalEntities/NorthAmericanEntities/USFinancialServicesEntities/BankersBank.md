---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bankers' bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commercial bank owned exclusively (except to the extent directors' qualifying shares are required by law) by other
      depository institutions or depository institution holding companies, the activities of which are limited by its articles
      of association exclusively to providing services to or for other depository institutions, their holding companies, and
      the officers, directors, and employees of such institutions and companies, and to providing correspondent banking services
      at the request of other depository institutions or their holding companies
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Depository Institutions Deregulation and Monetary Control Act of 1980, available at https://www.govinfo.gov/content/pkg/STATUTE-94/pdf/STATUTE-94-Pg132.pdf,
      section 711
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Bankers' banks are typically (1) organized solely to do business with other financial institutions (with the exceptions
      defined herein), (2) owned primarily by the financial institutions with which they conduct business, and (3) do not
      do business with the general public.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/isSubjectToReserveRequirements
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BankersBank
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: bankers' bank
type: Ontology Class
---

# bankers' bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BankersBank>

## Definition

commercial bank owned exclusively (except to the extent directors' qualifying shares are required by law) by other depository institutions or depository institution holding companies, the activities of which are limited by its articles of association exclusively to providing services to or for other depository institutions, their holding companies, and the officers, directors, and employees of such institutions and companies, and to providing correspondent banking services at the request of other depository institutions or their holding companies

## Relationships

- **Subclass of**: [CommercialBank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CommercialBank.md)
- **Subclass of**: [USBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md)

## Constraints

- **[isSubjectToReserveRequirements](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/isSubjectToReserveRequirements.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: bankers' bank
- **definition**: commercial bank owned exclusively (except to the extent directors' qualifying shares are required by law) by other depository institutions or depository institution holding companies, the activities of which are limited by its articles of association exclusively to providing services to or for other depository institutions, their holding companies, and the officers, directors, and employees of such institutions and companies, and to providing correspondent banking services at the request of other depository institutions or their holding companies
- **adaptedFrom**: Depository Institutions Deregulation and Monetary Control Act of 1980, available at https://www.govinfo.gov/content/pkg/STATUTE-94/pdf/STATUTE-94-Pg132.pdf, section 711
- **explanatoryNote**: Bankers' banks are typically (1) organized solely to do business with other financial institutions (with the exceptions defined herein), (2) owned primarily by the financial institutions with which they conduct business, and (3) do not do business with the general public.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
