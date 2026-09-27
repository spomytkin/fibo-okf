---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bullion
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical precious metal that is officially recognized as being at least 99.5 percent pure
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: In the United States, bullion that is eligible for reference in a commodities contract may include U.S. gold Buffalo
      coins minted by the U.S. Mint that are 1 troy ounce, 0.5 ounce, 0.25 ounce, or 0.10 ounce; 1 ounce silver coins; certain
      platinum coins; and gold, silver, palladium, and platinum bullion that meet or exceed the fineness requirements of a
      regulated futures contract. Bullion must also be certified by an approved certifier, typically identified by an exchange,
      including but not limited to the U.S. Mint.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Physical metals fall into two categories: (1) bullion, which are coins, ingots or bars of a specific weight and
      purity; and (2) "numismatic" or collectible coins, which can be rare or old coins, or special proofs that are newly
      minted as collectibles. If a particular asset is identified as "numismatic" or "collectible", it is, by definition,
      not considered bullion aside from its melt value.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/PreciousMetal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PreciousMetal
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/Bullion
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: bullion
type: Ontology Class
---

# bullion

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/Bullion>

## Definition

physical precious metal that is officially recognized as being at least 99.5 percent pure

## Relationships

- **Subclass of**: [PreciousMetal](/concepts/fibo/FND/Accounting/CurrencyAmount/PreciousMetal.md)

## Annotations

- **label** (en): bullion
- **definition** (en): physical precious metal that is officially recognized as being at least 99.5 percent pure
- **example** (en): In the United States, bullion that is eligible for reference in a commodities contract may include U.S. gold Buffalo coins minted by the U.S. Mint that are 1 troy ounce, 0.5 ounce, 0.25 ounce, or 0.10 ounce; 1 ounce silver coins; certain platinum coins; and gold, silver, palladium, and platinum bullion that meet or exceed the fineness requirements of a regulated futures contract. Bullion must also be certified by an approved certifier, typically identified by an exchange, including but not limited to the U.S. Mint.
- **explanatoryNote** (en): Physical metals fall into two categories: (1) bullion, which are coins, ingots or bars of a specific weight and purity; and (2) "numismatic" or collectible coins, which can be rare or old coins, or special proofs that are newly minted as collectibles. If a particular asset is identified as "numismatic" or "collectible", it is, by definition, not considered bullion aside from its melt value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
