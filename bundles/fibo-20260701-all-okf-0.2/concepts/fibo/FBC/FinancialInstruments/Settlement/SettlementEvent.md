---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: settlement event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specific event involving the finalization a transaction or portion thereof, including but not limited to finalizing
      accounting, exchanging consideration, and/or legally recording documents, as applicable
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/Settlement
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValueAssessment
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementEvent
sources:
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
title: settlement event
type: Ontology Class
---

# settlement event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementEvent>

## Definition

specific event involving the finalization a transaction or portion thereof, including but not limited to finalizing accounting, exchanging consideration, and/or legally recording documents, as applicable

## Relationships

- **Subclass of**: [ContractLifecycleEventOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md)

## Constraints

- **[hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)**: min qualified cardinality 0 of type [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [Settlement](/concepts/fibo/FBC/FinancialInstruments/Settlement/Settlement.md)
- **[involves](/concepts/fibo/FND/Relations/Relations/involves.md)**: min qualified cardinality 0 of type [ValueAssessment](/concepts/fibo/FND/Arrangements/Assessments/ValueAssessment.md)

## Annotations

- **label** (en): settlement event
- **definition**: specific event involving the finalization a transaction or portion thereof, including but not limited to finalizing accounting, exchanging consideration, and/or legally recording documents, as applicable

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
