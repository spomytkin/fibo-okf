---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Dow Jones Industrial Average value as of Mar 6, 2020
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual representing the value of the DJIA on 6 Mar 2020 at 12:05:14 pm in NYC
  - datatype: http://www.w3.org/2001/XMLSchema#decimal
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasRateValue
    value: '25523.20'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/hasQuotationDateTime
    value: '2020-03-06T12:05:14-05:00'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/NumericIndexValue
  related_to:
  - concept: /concepts/fibo/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverage.md
    predicate: https://www.omg.org/spec/Commons/QuantitiesAndUnits/isValueOf
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverage
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageValue-2023-03-06T120514-0500
sources:
- id: fibo-source-c9fb5c672c
  resource: references/fibo/EXMP/Securities/EquityIndexExamples.rdf
  sha256: c9fb5c672cbb6dc4ba551074dd33b7e27294259b5a24a6064670bc5c0205149d
  title: FIBO source EXMP/Securities/EquityIndexExamples.rdf
title: Dow Jones Industrial Average value as of Mar 6, 2020
type: Ontology Individual
---

# Dow Jones Industrial Average value as of Mar 6, 2020

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageValue-2023-03-06T120514-0500>

## Definition

individual representing the value of the DJIA on 6 Mar 2020 at 12:05:14 pm in NYC

## Relationships

- **Related to**: [DowJonesIndustrialAverage](/concepts/fibo/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverage.md)

## Annotations

- **label**: Dow Jones Industrial Average value as of Mar 6, 2020
- **definition**: individual representing the value of the DJIA on 6 Mar 2020 at 12:05:14 pm in NYC
- **hasRateValue**: 25523.20
- **hasQuotationDateTime**: 2020-03-06T12:05:14-05:00

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
