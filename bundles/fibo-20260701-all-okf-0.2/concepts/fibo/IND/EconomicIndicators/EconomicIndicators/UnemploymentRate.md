---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unemployment rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing the ratio of the unemployed population with respect to the civilian labor force
      of a given economy for some specified period
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.bls.gov/cps/faq.htm#Ques3
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Persons are classified as unemployed if they do not have a job, have actively looked for work in the prior 4 weeks,
      and are currently available for work. Workers expecting to be recalled from layoff are counted as unemployed, whether
      or not they have engaged in a specific jobseeking activity. In all other cases, the individual must have been engaged
      in at least one active job search activity in the 4 weeks preceding the interview and be available for work (except
      for temporary illness).
  - predicate: https://www.omg.org/spec/Commons/QuantitiesAndUnits/describesActualExpression
    value: unemployed population ÷ civilian labor force
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemployedPopulation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasComparisonPopulation
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.bls.gov/news.release/pdf/empsit.pdf
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: unemployment rate
type: Ontology Class
---

# unemployment rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate>

## Definition

economic indicator representing the ratio of the unemployed population with respect to the civilian labor force of a given economy for some specified period

## Relationships

- **See also**: [empsit.pdf](<http://www.bls.gov/news.release/pdf/empsit.pdf>)
- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasBaselinePopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation.md)**: some values from of type [CivilianLaborForce](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md)
- **[hasComparisonPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasComparisonPopulation.md)**: some values from of type [UnemployedPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/UnemployedPopulation.md)

## Annotations

- **label**: unemployment rate
- **definition**: economic indicator representing the ratio of the unemployed population with respect to the civilian labor force of a given economy for some specified period
- **adaptedFrom**: http://www.bls.gov/cps/faq.htm#Ques3
- **explanatoryNote**: Persons are classified as unemployed if they do not have a job, have actively looked for work in the prior 4 weeks, and are currently available for work. Workers expecting to be recalled from layoff are counted as unemployed, whether or not they have engaged in a specific jobseeking activity. In all other cases, the individual must have been engaged in at least one active job search activity in the 4 weeks preceding the interview and be available for work (except for temporary illness).
- **describesActualExpression**: unemployed population ÷ civilian labor force

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
