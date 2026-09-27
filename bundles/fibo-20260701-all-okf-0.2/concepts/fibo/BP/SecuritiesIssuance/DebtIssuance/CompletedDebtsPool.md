---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: completed debts pool
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/InIssuance
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/CompletedDebtsPool
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: completed debts pool
type: Ontology Class
---

# completed debts pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/CompletedDebtsPool>

## Relationships

- **Subclass of**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [InIssuance](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/InIssuance.md)

## Annotations

- **label** (en): completed debts pool

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
