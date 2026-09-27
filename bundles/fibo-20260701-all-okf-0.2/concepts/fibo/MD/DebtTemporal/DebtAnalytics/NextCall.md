---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: next call
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The next call of the issue, as at the current time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NextCallDate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDate
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallEvent
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NextCall
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: next call
type: Ontology Class
---

# next call

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NextCall>

## Definition

The next call of the issue, as at the current time.

## Relationships

- **Subclass of**: [CallEvent](/concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md)

## Constraints

- **[hasDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDate>)**: some values from of type [NextCallDate](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/NextCallDate.md)

## Annotations

- **label** (en): next call
- **definition** (en): The next call of the issue, as at the current time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
