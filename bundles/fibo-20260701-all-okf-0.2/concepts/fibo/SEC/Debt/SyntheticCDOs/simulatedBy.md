---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: simulated by
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The underlying CDS which is created to mechanise the cash flows in the synthetic portfolio.
  domain:
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticPoolAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticPoolAsset
  range:
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/simulatedBy
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: simulated by
type: Ontology Property
---

# simulated by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/simulatedBy>

## Definition

The underlying CDS which is created to mechanise the cash flows in the synthetic portfolio.

## Relationships

- **Domain**: [SyntheticPoolAsset](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticPoolAsset.md)
- **Range**: [CreditDefaultSwap](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)

## Annotations

- **label** (en): simulated by
- **definition** (en): The underlying CDS which is created to mechanise the cash flows in the synthetic portfolio.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
