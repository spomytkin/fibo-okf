---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: personal consumption expenditures
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing measure of the value of the goods and services purchased by, or on the behalf of,
      'persons'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: PCE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bea.gov/data/consumer-spending/main
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Personal consumption expenditures consist of purchases of goods and services by households and by nonprofit institutions
      serving households (NPISHs). These goods and services include imputed expenditures on items such as the services of
      housing by a homeowner (the equivalent of rent), financial and insurance services for which there is no explicit charge,
      and medical care provided to individuals and financed by government or by private insurance.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/PersonalConsumptionExpenditures
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: personal consumption expenditures
type: Ontology Class
---

# personal consumption expenditures

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/PersonalConsumptionExpenditures>

## Definition

economic indicator representing measure of the value of the goods and services purchased by, or on the behalf of, 'persons'

## Relationships

- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)

## Annotations

- **label**: personal consumption expenditures
- **definition**: economic indicator representing measure of the value of the goods and services purchased by, or on the behalf of, 'persons'
- **abbreviation**: PCE
- **adaptedFrom**: https://www.bea.gov/data/consumer-spending/main
- **explanatoryNote**: Personal consumption expenditures consist of purchases of goods and services by households and by nonprofit institutions serving households (NPISHs). These goods and services include imputed expenditures on items such as the services of housing by a homeowner (the equivalent of rent), financial and insurance services for which there is no explicit charge, and medical care provided to individuals and financed by government or by private insurance.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
