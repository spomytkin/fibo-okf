---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employment situation establishment survey
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: survey conducted on a regular basis that presents analytical information related to the labor force of a given
      statistical area, surveyed with respect to businesses, and is, for the most part, seasonally adjusted
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Establishment
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.bls.gov/news.release/empsit.tn.htm
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/EmploymentSituationSurvey.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/EmploymentSituationSurvey
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/EmploymentSituationEstablishmentSurvey
sources:
- id: fibo-source-6226f57562
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
  sha256: 6226f575629a4ee3c82b410564a799468e4879a8b2bae96e935c7a0a0ed2c6ac
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
title: employment situation establishment survey
type: Ontology Class
---

# employment situation establishment survey

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/EmploymentSituationEstablishmentSurvey>

## Definition

survey conducted on a regular basis that presents analytical information related to the labor force of a given statistical area, surveyed with respect to businesses, and is, for the most part, seasonally adjusted

## Relationships

- **See also**: [empsit.tn.htm](<https://www.bls.gov/news.release/empsit.tn.htm>)
- **Subclass of**: [EmploymentSituationSurvey](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/EmploymentSituationSurvey.md)

## Constraints

- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Establishment](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Establishment.md)

## Annotations

- **label**: employment situation establishment survey
- **definition**: survey conducted on a regular basis that presents analytical information related to the labor force of a given statistical area, surveyed with respect to businesses, and is, for the most part, seasonally adjusted
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
