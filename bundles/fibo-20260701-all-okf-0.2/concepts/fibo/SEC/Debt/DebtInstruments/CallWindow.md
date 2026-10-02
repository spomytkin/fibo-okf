---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: call window
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an explicit period of time prior to a call date during which an issuer or agent must give notice to holders
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallWindow
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: call window
type: Ontology Class
---

# call window

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallWindow>

## Definition

an explicit period of time prior to a call date during which an issuer or agent must give notice to holders

## Relationships

- **Subclass of**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label**: call window
- **definition**: an explicit period of time prior to a call date during which an issuer or agent must give notice to holders

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
