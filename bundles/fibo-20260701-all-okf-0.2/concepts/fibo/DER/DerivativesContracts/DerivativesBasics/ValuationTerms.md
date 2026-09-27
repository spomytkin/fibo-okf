---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: valuation terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms specific to valuation of the underlying asset(s)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasDateOfAssessment
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UnderlyingAssetValuation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ValuationTerms
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: valuation terms
type: Ontology Class
---

# valuation terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ValuationTerms>

## Definition

contract terms specific to valuation of the underlying asset(s)

## Relationships

- **Subclass of**: [DerivativeTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)

## Constraints

- **[hasDateOfAssessment](/concepts/fibo/FND/Arrangements/Assessments/hasDateOfAssessment.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[involves](/concepts/fibo/FND/Relations/Relations/involves.md)**: some values from of type [UnderlyingAssetValuation](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/UnderlyingAssetValuation.md)

## Annotations

- **label**: valuation terms
- **definition**: contract terms specific to valuation of the underlying asset(s)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
