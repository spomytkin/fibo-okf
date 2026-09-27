---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has put feature
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the specific terms related to any inherent put feature as specified in the offering/instrument
  range:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/PutFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutFeature
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/hasRepaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRepaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasPutFeature
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: has put feature
type: Ontology Property
---

# has put feature

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasPutFeature>

## Definition

indicates the specific terms related to any inherent put feature as specified in the offering/instrument

## Relationships

- **Range**: [PutFeature](/concepts/fibo/SEC/Debt/DebtInstruments/PutFeature.md)
- **Subproperty of**: [hasRepaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasRepaymentTerms.md)

## Annotations

- **label**: has put feature
- **definition**: indicates the specific terms related to any inherent put feature as specified in the offering/instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
