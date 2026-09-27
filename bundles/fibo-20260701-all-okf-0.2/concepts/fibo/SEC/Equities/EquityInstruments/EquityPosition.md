---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity position
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: position in an equity instrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholding
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwnedAsset
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholder
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/hasOwningParty
  - cardinality: 1
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Position.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Position
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityPosition
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: equity position
type: Ontology Class
---

# equity position

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityPosition>

## Definition

position in an equity instrument

## Relationships

- **Subclass of**: [Position](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Position.md)

## Constraints

- **[hasOwnedAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwnedAsset.md)**: some values from of type [Shareholding](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholding.md)
- **[hasOwningParty](/concepts/fibo/FND/OwnershipAndControl/Ownership/hasOwningParty.md)**: min qualified cardinality 0 of type [Shareholder](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md)
- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: exact qualified cardinality 1

## Annotations

- **label** (en): equity position
- **definition** (en): position in an equity instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
