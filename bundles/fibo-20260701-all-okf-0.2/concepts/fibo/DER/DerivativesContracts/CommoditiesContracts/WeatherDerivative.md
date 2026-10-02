---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weather derivative
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument whose primary underlying notional item is based on something related to the weather, for
      example, the average temperature in Chicago in January
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: CFTC glossary, https://www.cftc.gov/LearnAndProtect/EducationCenter/CFTCGlossary/glossary_wxyz.html
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the CFI standard, weather is classified as an environmental resource.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such a derivative can be used to hedge risks related to the demand for heating fuel or electricity. The underlying
      'asset' is not a negotiable commodity per se, but because the weather can impact the prices and other things related
      to other commodities, weather derivatives are treated as commodity derivatives for regulatory purposes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/WeatherDerivative
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: weather derivative
type: Ontology Class
---

# weather derivative

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/WeatherDerivative>

## Definition

derivative instrument whose primary underlying notional item is based on something related to the weather, for example, the average temperature in Chicago in January

## Relationships

- **Subclass of**: [CommodityDerivative](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Annotations

- **label**: weather derivative
- **definition** (en): derivative instrument whose primary underlying notional item is based on something related to the weather, for example, the average temperature in Chicago in January
- **adaptedFrom** (en): CFTC glossary, https://www.cftc.gov/LearnAndProtect/EducationCenter/CFTCGlossary/glossary_wxyz.html
- **explanatoryNote** (en): In the CFI standard, weather is classified as an environmental resource.
- **explanatoryNote** (en): Such a derivative can be used to hedge risks related to the demand for heating fuel or electricity. The underlying 'asset' is not a negotiable commodity per se, but because the weather can impact the prices and other things related to other commodities, weather derivatives are treated as commodity derivatives for regulatory purposes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
