---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Standard & Poor's Composite Index basket
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of common shares issued by approximately 500 large-cap companies that are traded on American stock exchanges
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSelectionCriteria
    value: To qualify for the S&P 500, a company must meet certain committee-established criteria, which include (1) a market
      cap of at least $13.1 billion, (2) trading the value of its market capitalization annually, (3) at least a quarter-million
      of its shares have been traded in each of the previous six months (4) the majority of shares are in the public's hands,
      (5) being publicly traded for at least a year, and (6) earnings over the most recent four quarters and in the most recent
      quarter must be positive.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/BasketOfEquities
  related_to:
  - concept: /concepts/fibo/EXMP/Securities/EquityIndexExamples/SPDowJonesIndicesLLC-US-DE.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSelectingParty
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/SPDowJonesIndicesLLC-US-DE
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/StandardAndPoors500CompositeIndexBasket
sources:
- id: fibo-source-c9fb5c672c
  resource: references/fibo/EXMP/Securities/EquityIndexExamples.rdf
  sha256: c9fb5c672cbb6dc4ba551074dd33b7e27294259b5a24a6064670bc5c0205149d
  title: FIBO source EXMP/Securities/EquityIndexExamples.rdf
title: Standard & Poor's Composite Index basket
type: Ontology Individual
---

# Standard & Poor's Composite Index basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/StandardAndPoors500CompositeIndexBasket>

## Definition

basket of common shares issued by approximately 500 large-cap companies that are traded on American stock exchanges

## Relationships

- **Related to**: [SPDowJonesIndicesLLC-US-DE](/concepts/fibo/EXMP/Securities/EquityIndexExamples/SPDowJonesIndicesLLC-US-DE.md)

## Annotations

- **label**: Standard & Poor's Composite Index basket
- **definition**: basket of common shares issued by approximately 500 large-cap companies that are traded on American stock exchanges
- **hasSelectionCriteria**: To qualify for the S&P 500, a company must meet certain committee-established criteria, which include (1) a market cap of at least $13.1 billion, (2) trading the value of its market capitalization annually, (3) at least a quarter-million of its shares have been traded in each of the previous six months (4) the majority of shares are in the public's hands, (5) being publicly traded for at least a year, and (6) earnings over the most recent four quarters and in the most recent quarter must be positive.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
