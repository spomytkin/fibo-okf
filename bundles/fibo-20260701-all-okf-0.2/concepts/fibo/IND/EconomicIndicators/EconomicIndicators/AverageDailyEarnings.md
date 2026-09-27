---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: average daily earnings
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of the average daily wage an employee makes over the reporting period
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=4360
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReferencePeriod
    value: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Daily
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/AverageEarnings.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/AverageEarnings
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/AverageDailyEarnings
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: average daily earnings
type: Ontology Class
---

# average daily earnings

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/AverageDailyEarnings>

## Definition

measure of the average daily wage an employee makes over the reporting period

## Relationships

- **Subclass of**: [AverageEarnings](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/AverageEarnings.md)

## Constraints

- **[hasReferencePeriod](/concepts/fibo/FND/Utilities/Analytics/hasReferencePeriod.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Daily`

## Annotations

- **label**: average daily earnings
- **definition**: measure of the average daily wage an employee makes over the reporting period
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=4360

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
