---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: gross domestic product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing the broadest measure of aggregate economic activity, measuring the total unduplicated
      market value of all final goods and services produced within a statistical area in a period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: GDP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: BEA's Handbook of Methods for GDP and related national accounts, available at https://www.bea.gov/methodologies/index.htm#national_meth
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Gross_domestic_product
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://home.treasury.gov/system/files/261/FSOC-2013-Annual-Report.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: GDP represents a valuation expressed in terms of the prices actually paid by the purchaser after all applicable
      taxes and subsidies.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Gross domestic product (GDP) is the value of the goods and services produced by the nation''s economy less the
      value of the goods and services used up in production. GDP is also equal to the sum of personal consumption expenditures,
      gross private domestic investment, net exports of goods and services, and government consumption expenditures and gross
      investment. Conceptually, this measure can be arrived at by three separate means: as the sum of goods and services sold
      to final users, as the sum of income payments and other costs incurred in the production of goods and services, and
      as the sum of the value added at each stage of production. Although these three ways of measuring GDP are conceptually
      the same, their calculation may not result in identical estimates of GDP because of differences in data sources, timing,
      and estimation techniques.'
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://unstats.un.org/unsd/nationalaccount/docs/SNA2008.pdf
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GrossDomesticProduct
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: gross domestic product
type: Ontology Class
---

# gross domestic product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GrossDomesticProduct>

## Definition

economic indicator representing the broadest measure of aggregate economic activity, measuring the total unduplicated market value of all final goods and services produced within a statistical area in a period

## Relationships

- **See also**: [SNA2008.pdf](<http://unstats.un.org/unsd/nationalaccount/docs/SNA2008.pdf>)
- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)

## Constraints

- **Disjoint with**: [UnemploymentRate](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate.md)

## Annotations

- **label**: gross domestic product
- **definition**: economic indicator representing the broadest measure of aggregate economic activity, measuring the total unduplicated market value of all final goods and services produced within a statistical area in a period
- **abbreviation**: GDP
- **adaptedFrom**: BEA's Handbook of Methods for GDP and related national accounts, available at https://www.bea.gov/methodologies/index.htm#national_meth
- **adaptedFrom**: https://en.wikipedia.org/wiki/Gross_domestic_product
- **adaptedFrom**: https://home.treasury.gov/system/files/261/FSOC-2013-Annual-Report.pdf
- **explanatoryNote**: GDP represents a valuation expressed in terms of the prices actually paid by the purchaser after all applicable taxes and subsidies.
- **explanatoryNote**: Gross domestic product (GDP) is the value of the goods and services produced by the nation's economy less the value of the goods and services used up in production. GDP is also equal to the sum of personal consumption expenditures, gross private domestic investment, net exports of goods and services, and government consumption expenditures and gross investment. Conceptually, this measure can be arrived at by three separate means: as the sum of goods and services sold to final users, as the sum of income payments and other costs incurred in the production of goods and services, and as the sum of the value added at each stage of production. Although these three ways of measuring GDP are conceptually the same, their calculation may not result in identical estimates of GDP because of differences in data sources, timing, and estimation techniques.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
