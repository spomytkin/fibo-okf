---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket credit default swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit default swap that references a bespoke, synthetic portfolio of underlying assets whose components have been
      agreed to for a specific OTC derivative by the parties to the transaction
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Draft paper on Credit Default Swaps from the Federal Reserve Board, available at https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/BasketCreditDefaultSwap
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: basket credit default swap
type: Ontology Class
---

# basket credit default swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/BasketCreditDefaultSwap>

## Definition

credit default swap that references a bespoke, synthetic portfolio of underlying assets whose components have been agreed to for a specific OTC derivative by the parties to the transaction

## Relationships

- **Subclass of**: [MultiNameCreditDefaultSwap](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap.md)

## Annotations

- **label** (en): basket credit default swap
- **definition** (en): credit default swap that references a bespoke, synthetic portfolio of underlying assets whose components have been agreed to for a specific OTC derivative by the parties to the transaction
- **adaptedFrom**: Draft paper on Credit Default Swaps from the Federal Reserve Board, available at https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
