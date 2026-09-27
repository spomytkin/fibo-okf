---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate cap option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest rate derivative in which the buyer receives payments at the end of each period in which the interest rate
      exceeds the agreed strike price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: An example of a cap would be an agreement to receive a payment for each month the LIBOR rate exceeds 2.5%.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The interest in each period is effectively capped by the strike rate. That is, the rate of interest may not go
      above the strike rate because the holder is expected to exercise the option to take the strike as the rate of interest
      instead.
  disjoint_with:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/InterestRateFloorOption.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/InterestRateFloorOption
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/InterestRateOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/InterestRateOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/InterestRateCapOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: interest rate cap option
type: Ontology Class
---

# interest rate cap option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/InterestRateCapOption>

## Definition

interest rate derivative in which the buyer receives payments at the end of each period in which the interest rate exceeds the agreed strike price

## Relationships

- **Subclass of**: [InterestRateOption](/concepts/fibo/DER/DerivativesContracts/Options/InterestRateOption.md)

## Constraints

- **Disjoint with**: [InterestRateFloorOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/InterestRateFloorOption.md)

## Annotations

- **label** (en): interest rate cap option
- **definition** (en): interest rate derivative in which the buyer receives payments at the end of each period in which the interest rate exceeds the agreed strike price
- **example** (en): An example of a cap would be an agreement to receive a payment for each month the LIBOR rate exceeds 2.5%.
- **explanatoryNote** (en): The interest in each period is effectively capped by the strike rate. That is, the rate of interest may not go above the strike rate because the holder is expected to exercise the option to take the strike as the rate of interest instead.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
