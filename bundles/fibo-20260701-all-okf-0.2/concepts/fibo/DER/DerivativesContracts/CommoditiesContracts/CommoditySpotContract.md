---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity spot contract
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract that involves physical delivery of the commodity asset at settlement
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019-10
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/SpotContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/SpotContract
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommoditySpotContract
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: commodity spot contract
type: Ontology Class
---

# commodity spot contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommoditySpotContract>

## Definition

contract that involves physical delivery of the commodity asset at settlement

## Relationships

- **Subclass of**: [CommodityInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument.md)
- **Subclass of**: [SpotContract](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/SpotContract.md)

## Annotations

- **label** (en): commodity spot contract
- **definition** (en): contract that involves physical delivery of the commodity asset at settlement
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
