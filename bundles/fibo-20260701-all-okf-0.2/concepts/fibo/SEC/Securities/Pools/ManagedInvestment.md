---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: managed investment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment pool that is controlled by a professional investment manager who invests the pool in various financial
      instruments and assets that align with their investment objectives and is overseen by a board of directors
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Bloomberg LP
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A managed investment is an investment vehicle that consists of a pool of funds collected from many different investors
      run by a management company.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: investment fund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isOpenEnded
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: managed investment
type: Ontology Class
---

# managed investment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment>

## Definition

investment pool that is controlled by a professional investment manager who invests the pool in various financial instruments and assets that align with their investment objectives and is overseen by a board of directors

## Relationships

- **Subclass of**: [CollectiveInvestmentVehicle](/concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)

## Constraints

- **[isOpenEnded](/concepts/fibo/SEC/Funds/Funds/isOpenEnded.md)**: some values from of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from of type [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label**: managed investment
- **definition**: investment pool that is controlled by a professional investment manager who invests the pool in various financial instruments and assets that align with their investment objectives and is overseen by a board of directors
- **adaptedFrom**: Bloomberg LP
- **adaptedFrom** (en): ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, October 2019
- **explanatoryNote** (en): A managed investment is an investment vehicle that consists of a pool of funds collected from many different investors run by a management company.
- **synonym** (en): investment fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
