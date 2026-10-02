---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dividend leg
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: floating leg of a dividend swap
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Note that both dividend swaps and some statistical swaps can be based on a dividend stream/leg.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N1b39e0e362a94d6ca990af35048bd976
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/SpecialDividendLegTerms
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/QualifyingDividendPeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SimpleReturnLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SimpleReturnLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/DividendLeg
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: dividend leg
type: Ontology Class
---

# dividend leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/DividendLeg>

## Definition

floating leg of a dividend swap

## Relationships

- **Subclass of**: [SimpleReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/SimpleReturnLeg.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N1b39e0e362a94d6ca990af35048bd976`
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: min qualified cardinality 0 of type [SpecialDividendLegTerms](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/SpecialDividendLegTerms.md)
- **[hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)**: some values from of type [QualifyingDividendPeriod](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/QualifyingDividendPeriod.md)

## Annotations

- **label** (en): dividend leg
- **definition** (en): floating leg of a dividend swap
- **usageNote** (en): Note that both dividend swaps and some statistical swaps can be based on a dividend stream/leg.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
