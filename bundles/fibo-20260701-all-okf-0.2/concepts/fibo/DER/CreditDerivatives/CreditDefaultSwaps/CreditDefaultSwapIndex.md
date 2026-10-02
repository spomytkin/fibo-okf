---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit default swap index
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: index whose underlying reference obligations are credit default swap instruments
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/BasketOfCreditDefaultSwaps
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/IND/MarketIndices/BasketIndices/ReferenceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/ReferenceIndex
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwapIndex
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: credit default swap index
type: Ontology Class
---

# credit default swap index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwapIndex>

## Definition

index whose underlying reference obligations are credit default swap instruments

## Relationships

- **Subclass of**: [ReferenceIndex](/concepts/fibo/IND/MarketIndices/BasketIndices/ReferenceIndex.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [BasketOfCreditDefaultSwaps](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/BasketOfCreditDefaultSwaps.md)

## Annotations

- **label** (en): credit default swap index
- **definition** (en): index whose underlying reference obligations are credit default swap instruments

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
