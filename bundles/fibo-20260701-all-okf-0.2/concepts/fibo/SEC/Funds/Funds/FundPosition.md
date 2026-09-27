---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund position
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: position in some fund, which may be defined in terms of fund units
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundHolding
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwnedAsset
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundHolder
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwningParty
  - cardinality: 1
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Position.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Position
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundPosition
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: fund position
type: Ontology Class
---

# fund position

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundPosition>

## Definition

position in some fund, which may be defined in terms of fund units

## Relationships

- **Subclass of**: [Position](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Position.md)

## Constraints

- **[hasOwnedAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwnedAsset.md)**: some values from of type [FundHolding](/concepts/fibo/SEC/Funds/Funds/FundHolding.md)
- **[hasOwningParty](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwningParty.md)**: min qualified cardinality 0 of type [FundHolder](/concepts/fibo/SEC/Funds/Funds/FundHolder.md)
- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: exact qualified cardinality 1

## Annotations

- **label** (en): fund position
- **definition** (en): position in some fund, which may be defined in terms of fund units

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
