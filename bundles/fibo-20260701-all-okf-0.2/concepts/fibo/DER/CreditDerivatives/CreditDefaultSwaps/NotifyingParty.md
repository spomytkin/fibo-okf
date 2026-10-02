---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: notifying party
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party responsible for issuing one or more formal notices indicating that an event that is relevant to a given contract
      has taken place
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The notifying party is the party that notifies the other party when a credit or other triggering event has occurred
      by means of a credit event notice. If more than one party is referenced as being the notifying party then either party
      may notify the other of such an occurrence.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/NotifyingParty
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: notifying party
type: Ontology Class
---

# notifying party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/NotifyingParty>

## Definition

party responsible for issuing one or more formal notices indicating that an event that is relevant to a given contract has taken place

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label** (en): notifying party
- **definition** (en): party responsible for issuing one or more formal notices indicating that an event that is relevant to a given contract has taken place
- **explanatoryNote** (en): The notifying party is the party that notifies the other party when a credit or other triggering event has occurred by means of a credit event notice. If more than one party is referenced as being the notifying party then either party may notify the other of such an occurrence.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
