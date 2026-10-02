---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: valuation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: method used to determine the present or expected worth of an asset
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Asset valuation is the process of determining the fair market or present value of assets, using book values, absolute
      valuation models like discounted cash flow analysis, option pricing models or comparables. Such assets include investments
      in marketable securities such as stocks, bonds and options; tangible assets like buildings and equipment; or intangible
      assets such as brands, patents and trademarks.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Strategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Strategy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValuationMethod
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: valuation method
type: Ontology Class
---

# valuation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValuationMethod>

## Definition

method used to determine the present or expected worth of an asset

## Relationships

- **Subclass of**: [Strategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Strategy.md)

## Annotations

- **label** (en): valuation method
- **definition** (en): method used to determine the present or expected worth of an asset
- **explanatoryNote** (en): Asset valuation is the process of determining the fair market or present value of assets, using book values, absolute valuation models like discounted cash flow analysis, option pricing models or comparables. Such assets include investments in marketable securities such as stocks, bonds and options; tangible assets like buildings and equipment; or intangible assets such as brands, patents and trademarks.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
