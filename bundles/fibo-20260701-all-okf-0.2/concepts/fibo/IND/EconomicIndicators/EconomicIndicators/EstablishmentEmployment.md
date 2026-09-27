---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: establishment employment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing the total number of persons who work in or for the establishment including working
      proprietors, active business partners and unpaid family workers, as well as persons working outside the establishment
      when paid by and under the control of the establishment, for example, sales representatives, outside service engineers
      and repair and maintenance personnel
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=780
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "Also included are salaried managers and salaried directors of incorporated enterprises. The total should include\
      \ part-time workers and seasonal workers on the payroll, persons on short-term leave (sick leave, maternity leave, annual\
      \ leave or vacation) and on strike, but not persons on indefinite leave, military leave or pension. \n\nExcluded are\
      \ directors of incorporated enterprises and members of shareholders committees who are paid solely for their attendance\
      \ at meetings, labour made available to the establishment by other units and charged for, such as contract workers paid\
      \ through contractors, persons carrying out repair and maintenance work in the establishment on behalf of other units\
      \ and all homeworkers."
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: payroll employment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EstablishmentPopulation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EstablishmentEmployment
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: establishment employment
type: Ontology Class
---

# establishment employment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EstablishmentEmployment>

## Definition

economic indicator representing the total number of persons who work in or for the establishment including working proprietors, active business partners and unpaid family workers, as well as persons working outside the establishment when paid by and under the control of the establishment, for example, sales representatives, outside service engineers and repair and maintenance personnel

## Relationships

- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasBaselinePopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation.md)**: some values from of type [EstablishmentPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EstablishmentPopulation.md)

## Annotations

- **label**: establishment employment
- **definition**: economic indicator representing the total number of persons who work in or for the establishment including working proprietors, active business partners and unpaid family workers, as well as persons working outside the establishment when paid by and under the control of the establishment, for example, sales representatives, outside service engineers and repair and maintenance personnel
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=780
- **explanatoryNote**: Also included are salaried managers and salaried directors of incorporated enterprises. The total should include part-time workers and seasonal workers on the payroll, persons on short-term leave (sick leave, maternity leave, annual leave or vacation) and on strike, but not persons on indefinite leave, military leave or pension.   Excluded are directors of incorporated enterprises and members of shareholders committees who are paid solely for their attendance at meetings, labour made available to the establishment by other units and charged for, such as contract workers paid through contractors, persons carrying out repair and maintenance work in the establishment on behalf of other units and all homeworkers.
- **synonym**: payroll employment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
