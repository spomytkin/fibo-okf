---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: specifies conversion into
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a security that will replace a convertible security under the terms of the agreement
  domain:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/ConversionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConversionTerms
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/specifiesConversionInto
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: specifies conversion into
type: Ontology Property
---

# specifies conversion into

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/specifiesConversionInto>

## Definition

specifies a security that will replace a convertible security under the terms of the agreement

## Relationships

- **Domain**: [ConversionTerms](/concepts/fibo/SEC/Securities/SecuritiesIssuance/ConversionTerms.md)
- **Range**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label**: specifies conversion into
- **definition**: specifies a security that will replace a convertible security under the terms of the agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
