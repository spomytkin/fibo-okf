---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exposure situation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: state of affairs in which some party is subject to influence or risk arising from a specific contract, instrument,
      or arrangement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasExposedParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasExposureTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: exposure situation
type: Ontology Class
---

# exposure situation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation>

## Definition

state of affairs in which some party is subject to influence or risk arising from a specific contract, instrument, or arrangement

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[hasExposedParty](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasExposedParty.md)**: some values from of type [ExposureBearer](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer.md)
- **[hasExposureTo](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasExposureTo.md)**: some values from of type [Exposure](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md)

## Annotations

- **label** (en): exposure situation
- **definition**: state of affairs in which some party is subject to influence or risk arising from a specific contract, instrument, or arrangement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
