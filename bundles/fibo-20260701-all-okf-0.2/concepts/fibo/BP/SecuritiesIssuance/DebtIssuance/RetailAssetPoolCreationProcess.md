---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: retail asset pool creation process
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The process by which pools of assets are created. These may then be used in the issue of securities based on those
      asset pools as underlying.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isProducedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcess
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/precedes
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/AssetPoolCreationProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/AssetPoolCreationProcess
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/RetailAssetPoolCreationProcess
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: retail asset pool creation process
type: Ontology Class
---

# retail asset pool creation process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/RetailAssetPoolCreationProcess>

## Definition

The process by which pools of assets are created. These may then be used in the issue of securities based on those asset pools as underlying.

## Relationships

- **Subclass of**: [AssetPoolCreationProcess](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/AssetPoolCreationProcess.md)

## Constraints

- **[isProducedBy](/concepts/fibo/FND/Relations/Relations/isProducedBy.md)**: some values from of type [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)
- **[precedes](<https://www.omg.org/spec/Commons/DatesAndTimes/precedes>)**: some values from of type [PoolBackedSecuritySecuritizationProcess](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcess.md)

## Annotations

- **label** (en): retail asset pool creation process
- **definition** (en): The process by which pools of assets are created. These may then be used in the issue of securities based on those asset pools as underlying.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
