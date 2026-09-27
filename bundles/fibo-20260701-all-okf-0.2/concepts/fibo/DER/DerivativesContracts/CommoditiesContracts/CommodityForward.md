---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity forward
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: forward contract in which a buyer and seller agree upon delivery of a specified quality and quantity of goods at
      a specified future date
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: CFTC glossary
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019-10
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Commodity forwards are often settled via cash transactions in many industries, including for the purposes of commodity
      merchandising. Terms may be more "personalized" than is the case with standardized futures contracts (i.e., delivery
      time and amount are as determined between seller and buyer). A price may be agreed upon in advance, or there may be
      agreement that the price will be determined at the time of delivery. A forward contract is a private and customizable
      agreement that settles at the end of the agreement and is traded over-the-counter.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/Forward.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/Forward
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityForward
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: commodity forward
type: Ontology Class
---

# commodity forward

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityForward>

## Definition

forward contract in which a buyer and seller agree upon delivery of a specified quality and quantity of goods at a specified future date

## Relationships

- **Subclass of**: [CommodityDerivative](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- **Subclass of**: [Forward](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/Forward.md)

## Annotations

- **label** (en): commodity forward
- **definition** (en): forward contract in which a buyer and seller agree upon delivery of a specified quality and quantity of goods at a specified future date
- **adaptedFrom** (en): CFTC glossary
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10
- **explanatoryNote** (en): Commodity forwards are often settled via cash transactions in many industries, including for the purposes of commodity merchandising. Terms may be more "personalized" than is the case with standardized futures contracts (i.e., delivery time and amount are as determined between seller and buyer). A price may be agreed upon in advance, or there may be agreement that the price will be determined at the time of delivery. A forward contract is a private and customizable agreement that settles at the end of the agreement and is traded over-the-counter.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
