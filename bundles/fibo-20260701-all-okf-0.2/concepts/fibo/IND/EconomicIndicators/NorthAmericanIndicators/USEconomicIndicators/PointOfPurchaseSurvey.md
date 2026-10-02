---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: point of purchase survey
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a program conducted on a regular basis that provides information on purchases of various items and services by
      consumers
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: http://www.bls.gov/respondents/cpi/tpops/
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalProgram.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalProgram
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/PointOfPurchaseSurvey
sources:
- id: fibo-source-6226f57562
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
  sha256: 6226f575629a4ee3c82b410564a799468e4879a8b2bae96e935c7a0a0ed2c6ac
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
title: point of purchase survey
type: Ontology Class
---

# point of purchase survey

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/PointOfPurchaseSurvey>

## Definition

a program conducted on a regular basis that provides information on purchases of various items and services by consumers

## Relationships

- **Related to**: [tpops](<http://www.bls.gov/respondents/cpi/tpops/>)
- **Subclass of**: [StatisticalProgram](/concepts/fibo/FND/Utilities/Analytics/StatisticalProgram.md)

## Annotations

- **label**: point of purchase survey
- **definition**: a program conducted on a regular basis that provides information on purchases of various items and services by consumers

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
