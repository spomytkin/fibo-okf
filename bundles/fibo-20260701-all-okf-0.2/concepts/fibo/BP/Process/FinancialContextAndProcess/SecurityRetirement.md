---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security retirement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/isRetirementOf
resource: https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/SecurityRetirement
sources:
- id: fibo-source-0e9d52107c
  resource: references/fibo/BP/Process/FinancialContextAndProcess.rdf
  sha256: 0e9d52107c2c95399af0cae6beab257d8f221907647b9df5caa05d479e71785a
  title: FIBO source BP/Process/FinancialContextAndProcess.rdf
title: security retirement
type: Ontology Class
---

# security retirement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/SecurityRetirement>

## Constraints

- **[isRetirementOf](/concepts/fibo/BP/Process/FinancialContextAndProcess/isRetirementOf.md)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label** (en): security retirement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
