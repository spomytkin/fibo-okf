---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: right to retain
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the holder has an option to retain the security in the event of an issuer exercising the put
      feature
  domain:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/PutFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutFeature
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRightToRetain
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: right to retain
type: Ontology Property
---

# right to retain

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRightToRetain>

## Definition

indicates whether the holder has an option to retain the security in the event of an issuer exercising the put feature

## Relationships

- **Domain**: [PutFeature](/concepts/fibo/SEC/Debt/DebtInstruments/PutFeature.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: right to retain
- **definition**: indicates whether the holder has an option to retain the security in the event of an issuer exercising the put feature

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
