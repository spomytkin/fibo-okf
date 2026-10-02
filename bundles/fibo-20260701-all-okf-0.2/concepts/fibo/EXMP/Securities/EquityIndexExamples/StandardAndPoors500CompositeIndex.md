---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Standard & Poor's Composite Index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: equity index that is calculated based on the float-adjusted market capitalization of approximately 500 large companies
      listed on stock exchanges in the United States
  - language: en
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/isCalculatedViaMethodology
    value: 'The components of the S&P 500 are selected by a committee. When considering the eligibility of a new addition,
      the committee assesses the company''s merit using eight primary criteria: market capitalization, liquidity, domicile,
      public float, sector classification, financial viability, and length of time publicly traded and stock exchange.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: S&P 500
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The S&P 500 is a market capitalization-weighted index and the performance of the 10 largest companies in the index
      account for 21.8 percent of the performance of the index.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/EquityIndex
  related_to:
  - concept: /concepts/fibo/EXMP/Securities/EquityIndexExamples/SPDowJonesIndices.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/SPDowJonesIndices
  - concept: /concepts/fibo/EXMP/Securities/EquityIndexExamples/StandardAndPoors500CompositeIndexBasket.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/StandardAndPoors500CompositeIndexBasket
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/StandardAndPoors500CompositeIndex
sources:
- id: fibo-source-c9fb5c672c
  resource: references/fibo/EXMP/Securities/EquityIndexExamples.rdf
  sha256: c9fb5c672cbb6dc4ba551074dd33b7e27294259b5a24a6064670bc5c0205149d
  title: FIBO source EXMP/Securities/EquityIndexExamples.rdf
title: Standard & Poor's Composite Index
type: Ontology Individual
---

# Standard & Poor's Composite Index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/StandardAndPoors500CompositeIndex>

## Definition

equity index that is calculated based on the float-adjusted market capitalization of approximately 500 large companies listed on stock exchanges in the United States

## Relationships

- **Related to**: [SPDowJonesIndices](/concepts/fibo/EXMP/Securities/EquityIndexExamples/SPDowJonesIndices.md)
- **Related to**: [StandardAndPoors500CompositeIndexBasket](/concepts/fibo/EXMP/Securities/EquityIndexExamples/StandardAndPoors500CompositeIndexBasket.md)

## Annotations

- **label**: Standard & Poor's Composite Index
- **definition**: equity index that is calculated based on the float-adjusted market capitalization of approximately 500 large companies listed on stock exchanges in the United States
- **isCalculatedViaMethodology** (en): The components of the S&P 500 are selected by a committee. When considering the eligibility of a new addition, the committee assesses the company's merit using eight primary criteria: market capitalization, liquidity, domicile, public float, sector classification, financial viability, and length of time publicly traded and stock exchange.
- **abbreviation**: S&P 500
- **explanatoryNote** (en): The S&P 500 is a market capitalization-weighted index and the performance of the 10 largest companies in the index account for 21.8 percent of the performance of the index.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
