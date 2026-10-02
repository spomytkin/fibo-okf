---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: settlement auction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: independently administered synthetic auction process on a set of defined deliverable obligations that sets the
      reference final price that can be used to facilitate cash settlement of all covered transactions following a credit
      event
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/Settlement/SettlementEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementEvent
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/SettlementAuction
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: settlement auction
type: Ontology Class
---

# settlement auction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/SettlementAuction>

## Definition

independently administered synthetic auction process on a set of defined deliverable obligations that sets the reference final price that can be used to facilitate cash settlement of all covered transactions following a credit event

## Relationships

- **Subclass of**: [SettlementEvent](/concepts/fibo/FBC/FinancialInstruments/Settlement/SettlementEvent.md)

## Annotations

- **label** (en): settlement auction
- **definition** (en): independently administered synthetic auction process on a set of defined deliverable obligations that sets the reference final price that can be used to facilitate cash settlement of all covered transactions following a credit event
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
