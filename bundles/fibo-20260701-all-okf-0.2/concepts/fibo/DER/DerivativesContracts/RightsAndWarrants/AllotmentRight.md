---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: allotment right
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: privileges allotted to existing security holders, entitling them to receive new securities free of charge
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Allotment generally means the distribution of equity, particularly shares granted to a participating underwriting
      firm during an initial public offering (IPO).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bonus right
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/AllotmentRightFormula
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/AllotmentRight
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: allotment right
type: Ontology Class
---

# allotment right

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/AllotmentRight>

## Definition

privileges allotted to existing security holders, entitling them to receive new securities free of charge

## Relationships

- **Subclass of**: [EquityDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md)
- **Subclass of**: [Entitlement](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)

## Constraints

- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: some values from of type [AllotmentRightFormula](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/AllotmentRightFormula.md)

## Annotations

- **label** (en): allotment right
- **definition** (en): privileges allotted to existing security holders, entitling them to receive new securities free of charge
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): Allotment generally means the distribution of equity, particularly shares granted to a participating underwriting firm during an initial public offering (IPO).
- **synonym** (en): bonus right

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
