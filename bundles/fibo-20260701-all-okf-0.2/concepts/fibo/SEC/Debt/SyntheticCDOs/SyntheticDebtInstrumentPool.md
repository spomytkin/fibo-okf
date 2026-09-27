---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: synthetic debt instrument pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A cash flow structure which synthesizes the behavior of a portfolio of debt securities. For example a synthesized
      portfolio of CDO / Bonds / ABS using Total Returns Swaps and CDS. This does exist, it is just manufactured from different
      instruments.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/fundedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/hasUnderlyingContract
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOPortfolio
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/makesReferenceTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPool
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: synthetic debt instrument pool
type: Ontology Class
---

# synthetic debt instrument pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPool>

## Definition

A cash flow structure which synthesizes the behavior of a portfolio of debt securities. For example a synthesized portfolio of CDO / Bonds / ABS using Total Returns Swaps and CDS. This does exist, it is just manufactured from different instruments.

## Relationships

- **Subclass of**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Constraints

- **[fundedBy](/concepts/fibo/SEC/Debt/SyntheticCDOs/fundedBy.md)**: some values from of type [SyntheticDebtInstrumentPoolFundingAsset](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset.md)
- **[hasUnderlyingContract](/concepts/fibo/SEC/Debt/SyntheticCDOs/hasUnderlyingContract.md)**: some values from of type [CreditDefaultSwap](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)
- **[makesReferenceTo](/concepts/fibo/SEC/Debt/SyntheticCDOs/makesReferenceTo.md)**: some values from of type [SyntheticCDOPortfolio](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOPortfolio.md)

## Annotations

- **label** (en): synthetic debt instrument pool
- **definition** (en): A cash flow structure which synthesizes the behavior of a portfolio of debt securities. For example a synthesized portfolio of CDO / Bonds / ABS using Total Returns Swaps and CDS. This does exist, it is just manufactured from different instruments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
