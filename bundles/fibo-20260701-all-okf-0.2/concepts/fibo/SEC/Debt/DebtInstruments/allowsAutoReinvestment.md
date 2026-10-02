---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: allows auto-reinvestment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the security allows automatically re-investing the interest on that security towards purchasing
      additional shares or units of the same security
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/allowsAutoReinvestment
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: allows auto-reinvestment
type: Ontology Property
---

# allows auto-reinvestment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/allowsAutoReinvestment>

## Definition

indicates whether the security allows automatically re-investing the interest on that security towards purchasing additional shares or units of the same security

## Relationships

- **Domain**: [InterestPaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: allows auto-reinvestment
- **definition**: indicates whether the security allows automatically re-investing the interest on that security towards purchasing additional shares or units of the same security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
