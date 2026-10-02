---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Dow Jones Industrial Average
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: equity index of 30 substantial stocks that are traded on the New York Stock Exchange (NYSE) and the Nasdaq
  - language: en
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/isCalculatedViaMethodology
    value: The index is calculated by adding the price of a single share of each stock together, with equal weighting, and
      dividing by the Dow Divisor which is constantly adjusted, and is currently around 0.1474.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: DJIA
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: Dow
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: ''
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/EquityIndex
  related_to:
  - concept: /concepts/fibo/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket
  - concept: /concepts/fibo/EXMP/Securities/EquityIndexExamples/SPDowJonesIndices.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/SPDowJonesIndices
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverage
sources:
- id: fibo-source-c9fb5c672c
  resource: references/fibo/EXMP/Securities/EquityIndexExamples.rdf
  sha256: c9fb5c672cbb6dc4ba551074dd33b7e27294259b5a24a6064670bc5c0205149d
  title: FIBO source EXMP/Securities/EquityIndexExamples.rdf
title: Dow Jones Industrial Average
type: Ontology Individual
---

# Dow Jones Industrial Average

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverage>

## Definition

equity index of 30 substantial stocks that are traded on the New York Stock Exchange (NYSE) and the Nasdaq

## Relationships

- **Related to**: [SPDowJonesIndices](/concepts/fibo/EXMP/Securities/EquityIndexExamples/SPDowJonesIndices.md)
- **Related to**: [DowJonesIndustrialAverageBasket](/concepts/fibo/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket.md)

## Annotations

- **label**: Dow Jones Industrial Average
- **definition**: equity index of 30 substantial stocks that are traded on the New York Stock Exchange (NYSE) and the Nasdaq
- **isCalculatedViaMethodology** (en): The index is calculated by adding the price of a single share of each stock together, with equal weighting, and dividing by the Dow Divisor which is constantly adjusted, and is currently around 0.1474.
- **abbreviation**: DJIA
- **abbreviation**: Dow
- **explanatoryNote** (en): 

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
