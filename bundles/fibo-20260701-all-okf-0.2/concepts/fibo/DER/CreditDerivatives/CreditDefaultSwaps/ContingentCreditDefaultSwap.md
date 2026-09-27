---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contingent credit default swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit default swap in which an additional triggering event is required
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CCDS
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a contingent credit default swap, the trigger requires both a credit event (as in a traditional credit default
      swap) and another specified event. The additional specified event is usually a significant movement in an index covering
      equities, commodities, interest rates, or some other overall measure of the economy or relevant industry.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/ContingentCreditDefaultSwap
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: contingent credit default swap
type: Ontology Class
---

# contingent credit default swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/ContingentCreditDefaultSwap>

## Definition

credit default swap in which an additional triggering event is required

## Relationships

- **Subclass of**: [CreditDefaultSwap](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)

## Annotations

- **label** (en): contingent credit default swap
- **definition** (en): credit default swap in which an additional triggering event is required
- **abbreviation** (en): CCDS
- **explanatoryNote** (en): In a contingent credit default swap, the trigger requires both a credit event (as in a traditional credit default swap) and another specified event. The additional specified event is usually a significant movement in an index covering equities, commodities, interest rates, or some other overall measure of the economy or relevant industry.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
