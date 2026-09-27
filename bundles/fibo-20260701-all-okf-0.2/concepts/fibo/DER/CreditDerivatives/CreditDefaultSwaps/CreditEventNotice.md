---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit event notice
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: irrevocable written or verbal notice that states that a triggering event has occurred
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Notices of certain kinds of credit events are required as a condition of a credit default swap. Such notices are
      sent from a notifying party (either the buyer or the seller) to the counterparty. They provide information that assists
      the contract parties in determining whether a triggering credit event has occurred.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/NotifyingParty
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Notice
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditEventNotice
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: credit event notice
type: Ontology Class
---

# credit event notice

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditEventNotice>

## Definition

irrevocable written or verbal notice that states that a triggering event has occurred

## Relationships

- **Subclass of**: [Notice](<https://www.omg.org/spec/Commons/Documents/Notice>)

## Constraints

- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [TriggeringEvent](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [NotifyingParty](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/NotifyingParty.md)

## Annotations

- **label** (en): credit event notice
- **definition** (en): irrevocable written or verbal notice that states that a triggering event has occurred
- **explanatoryNote** (en): Notices of certain kinds of credit events are required as a condition of a credit default swap. Such notices are sent from a notifying party (either the buyer or the seller) to the counterparty. They provide information that assists the contract parties in determining whether a triggering credit event has occurred.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
