---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: maximum amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'This has not been seen - incliuded as it''s implicit but we might want to get rid of this. ACTION: Look at example
      prospectus document, mark up against this model; if this item is not seen, we could remove it'
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TrancheNotesParameters.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TrancheNotesParameters
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/maximumAmount
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: maximum amount
type: Ontology Property
---

# maximum amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/maximumAmount>

## Definition

This has not been seen - incliuded as it's implicit but we might want to get rid of this. ACTION: Look at example prospectus document, mark up against this model; if this item is not seen, we could remove it

## Relationships

- **Domain**: [TrancheNotesParameters](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TrancheNotesParameters.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): maximum amount
- **definition** (en): This has not been seen - incliuded as it's implicit but we might want to get rid of this. ACTION: Look at example prospectus document, mark up against this model; if this item is not seen, we could remove it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
