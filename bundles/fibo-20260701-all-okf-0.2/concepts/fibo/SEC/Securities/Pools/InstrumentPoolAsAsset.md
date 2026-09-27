---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: instrument pool as asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial asset in the form of an instrument pool
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isAssetOf
    value: N4ddc28e8e9f84bc0afc560e4b18b4860
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/InstrumentPool
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/InstrumentPoolAsAsset
sources:
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: instrument pool as asset
type: Ontology Class
---

# instrument pool as asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/InstrumentPoolAsAsset>

## Definition

financial asset in the form of an instrument pool

## Relationships

- **Subclass of**: [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)

## Constraints

- **[isAssetOf](/concepts/fibo/FND/OwnershipAndControl/Ownership/isAssetOf.md)**: some values from value `N4ddc28e8e9f84bc0afc560e4b18b4860`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [InstrumentPool](/concepts/fibo/SEC/Securities/Pools/InstrumentPool.md)

## Annotations

- **label**: instrument pool as asset
- **definition**: financial asset in the form of an instrument pool

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
