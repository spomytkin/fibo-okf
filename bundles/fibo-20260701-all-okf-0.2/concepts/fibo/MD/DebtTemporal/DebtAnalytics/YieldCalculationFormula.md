---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: yield calculation formula
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The formula used in determining the Yield.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The subject of this Formula is the Yield. The formula has an expression which can be defined either in tectual
      terms or by further local extension of the term "Formula Expression" to define the parameters used.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Formula.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Formula
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: yield calculation formula
type: Ontology Class
---

# yield calculation formula

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula>

## Definition

The formula used in determining the Yield.

## Relationships

- **Subclass of**: [Formula](/concepts/fibo/FND/Utilities/Analytics/Formula.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)

## Annotations

- **label** (en): yield calculation formula
- **definition** (en): The formula used in determining the Yield.
- **explanatoryNote** (en): The subject of this Formula is the Yield. The formula has an expression which can be defined either in tectual terms or by further local extension of the term "Formula Expression" to define the parameters used.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
