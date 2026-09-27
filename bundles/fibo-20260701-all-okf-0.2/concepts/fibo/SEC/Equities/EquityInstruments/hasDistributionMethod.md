---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has distribution method
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the method by which dividend payments are to be distributed
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
  range:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/DividendDistributionMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/DividendDistributionMethod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDistributionMethod
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has distribution method
type: Ontology Property
---

# has distribution method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDistributionMethod>

## Definition

indicates the method by which dividend payments are to be distributed

## Relationships

- **Domain**: [Dividend](/concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md)
- **Range**: [DividendDistributionMethod](/concepts/fibo/SEC/Equities/EquityInstruments/DividendDistributionMethod.md)
- **Subproperty of**: [hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)

## Annotations

- **label**: has distribution method
- **definition**: indicates the method by which dividend payments are to be distributed

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
