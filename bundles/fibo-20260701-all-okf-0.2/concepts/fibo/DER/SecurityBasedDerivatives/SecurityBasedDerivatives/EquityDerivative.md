---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity derivative
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security-based derivative whose underlier is based on equities (e.g. shares, basket of equities or index) or their
      cashflow(s)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N2c6e0a1c42bf4447a96f2e8610c4d3e1
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative
sources:
- id: fibo-source-e409c614fa
  resource: references/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
  sha256: e409c614fa05cf3a92ef2ffb652008525612be13fc2347acd6b082fe0f4dc330
  title: FIBO source DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
title: equity derivative
type: Ontology Class
---

# equity derivative

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative>

## Definition

security-based derivative whose underlier is based on equities (e.g. shares, basket of equities or index) or their cashflow(s)

## Relationships

- **Subclass of**: [SecurityBasedDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N2c6e0a1c42bf4447a96f2e8610c4d3e1`

## Annotations

- **label**: equity derivative
- **definition**: security-based derivative whose underlier is based on equities (e.g. shares, basket of equities or index) or their cashflow(s)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
