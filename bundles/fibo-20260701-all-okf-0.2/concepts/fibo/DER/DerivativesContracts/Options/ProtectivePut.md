---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: protective put
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: put option giving the buyer (holder) the right, but not the obligation, to sell the assets specified at with a
      strike price equal or close to the current price of the underlying asset, on or before a specified date
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A protective put is a risk management and options strategy that involves holding a long position in the underlying
      asset (e.g., stock). A protective put strategy is analogous to the nature of insurance. The main goal of a protective
      put is to limit potential losses that may result from an unexpected price drop of the underlying asset
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: synthetic call
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionPremium
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasCalculatedMarketValue
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/PutOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/PutOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ProtectivePut
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: protective put
type: Ontology Class
---

# protective put

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ProtectivePut>

## Definition

put option giving the buyer (holder) the right, but not the obligation, to sell the assets specified at with a strike price equal or close to the current price of the underlying asset, on or before a specified date

## Relationships

- **Subclass of**: [PutOption](/concepts/fibo/DER/DerivativesContracts/Options/PutOption.md)

## Constraints

- **[hasCalculatedMarketValue](/concepts/fibo/DER/DerivativesContracts/Options/hasCalculatedMarketValue.md)**: some values from of type [OptionPremium](/concepts/fibo/DER/DerivativesContracts/Options/OptionPremium.md)

## Annotations

- **label** (en): protective put
- **definition** (en): put option giving the buyer (holder) the right, but not the obligation, to sell the assets specified at with a strike price equal or close to the current price of the underlying asset, on or before a specified date
- **explanatoryNote** (en): A protective put is a risk management and options strategy that involves holding a long position in the underlying asset (e.g., stock). A protective put strategy is analogous to the nature of insurance. The main goal of a protective put is to limit potential losses that may result from an unexpected price drop of the underlying asset
- **synonym** (en): synthetic call

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
