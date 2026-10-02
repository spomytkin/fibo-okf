---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: synthetic balance sheet c d o
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/issues
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/BalanceSheetCDO.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/BalanceSheetCDO
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDO.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDO
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticBalanceSheetCDO
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: synthetic balance sheet c d o
type: Ontology Class
---

# synthetic balance sheet c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticBalanceSheetCDO>

## Relationships

- **Subclass of**: [BalanceSheetCDO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/BalanceSheetCDO.md)
- **Subclass of**: [SyntheticCDO](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDO.md)

## Constraints

- **[issues](/concepts/fibo/SEC/Debt/SyntheticCDOs/issues.md)**: some values from of type [SyntheticCDOTranche](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md)

## Annotations

- **label** (en): synthetic balance sheet c d o

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
