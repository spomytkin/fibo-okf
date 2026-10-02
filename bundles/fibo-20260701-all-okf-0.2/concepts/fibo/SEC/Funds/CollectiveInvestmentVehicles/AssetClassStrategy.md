---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: asset class strategy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Strategy which is asset class based.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'EFAMA: The type of securities or other holdings that may be invested in. FIBIM: Strategy which is asset class
      based. Can implement this in terms of a classification of those things. Wording implies this is a policy.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/identifiesAssetTypesBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/AssetClassStrategy
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: asset class strategy
type: Ontology Class
---

# asset class strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/AssetClassStrategy>

## Definition

Strategy which is asset class based.

## Relationships

- **Subclass of**: [FundPortfolioInvestmentLimitations](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md)

## Constraints

- **[identifiesAssetTypesBy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/identifiesAssetTypesBy.md)**: some values from of type [FinancialInstrumentClassifier](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)

## Annotations

- **label** (en): asset class strategy
- **definition** (en): Strategy which is asset class based.
- **explanatoryNote** (en): EFAMA: The type of securities or other holdings that may be invested in. FIBIM: Strategy which is asset class based. Can implement this in terms of a classification of those things. Wording implies this is a policy.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
