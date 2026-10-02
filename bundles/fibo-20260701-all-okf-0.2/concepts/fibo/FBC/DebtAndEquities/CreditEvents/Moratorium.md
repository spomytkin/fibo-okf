---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: moratorium
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entity-specific credit event involving a temporary suspension of payments until related issues are resolved
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A moratorium may be a legally-mandated hiatus in debt collection as a part of a bankruptcy process.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/Moratorium
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: moratorium
type: Ontology Class
---

# moratorium

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/Moratorium>

## Definition

entity-specific credit event involving a temporary suspension of payments until related issues are resolved

## Relationships

- **Subclass of**: [EntitySpecificCreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent.md)

## Annotations

- **label** (en): moratorium
- **definition** (en): entity-specific credit event involving a temporary suspension of payments until related issues are resolved
- **explanatoryNote** (en): A moratorium may be a legally-mandated hiatus in debt collection as a part of a bankruptcy process.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
