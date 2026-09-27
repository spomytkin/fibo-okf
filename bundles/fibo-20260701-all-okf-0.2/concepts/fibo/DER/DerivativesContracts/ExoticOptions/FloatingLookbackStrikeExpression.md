---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: floating lookback strike expression
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cashflow expression specifying the arguments required to calculate the best projected price at which the lookback
      option may be exercised
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ProjectedValueAtMaturity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasMinuend
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ObservedBestValue
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasSubtrahend
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CashflowExpression.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CashflowExpression
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/FloatingLookbackStrikeExpression
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: floating lookback strike expression
type: Ontology Class
---

# floating lookback strike expression

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/FloatingLookbackStrikeExpression>

## Definition

cashflow expression specifying the arguments required to calculate the best projected price at which the lookback option may be exercised

## Relationships

- **Subclass of**: [CashflowExpression](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/CashflowExpression.md)

## Constraints

- **[hasMinuend](/concepts/fibo/FND/Utilities/Analytics/hasMinuend.md)**: some values from of type [ProjectedValueAtMaturity](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/ProjectedValueAtMaturity.md)
- **[hasSubtrahend](/concepts/fibo/FND/Utilities/Analytics/hasSubtrahend.md)**: some values from of type [ObservedBestValue](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/ObservedBestValue.md)

## Annotations

- **label** (en): floating lookback strike expression
- **definition** (en): cashflow expression specifying the arguments required to calculate the best projected price at which the lookback option may be exercised

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
