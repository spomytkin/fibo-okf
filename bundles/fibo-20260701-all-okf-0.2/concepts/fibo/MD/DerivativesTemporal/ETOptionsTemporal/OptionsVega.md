---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: options vega
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'A measure of the rate of change in an option''s theoretical value for a one-unit change in the volatility assumption.
      Action: add terms that define or influence this.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionTheoreticalValue
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/MD/DerivativesTemporal/ETOptionsTemporal/OptionsGreek.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionsGreek
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionsVega
sources:
- id: fibo-source-c9fb3c7ad1
  resource: references/fibo/MD/DerivativesTemporal/ETOptionsTemporal.rdf
  sha256: c9fb3c7ad151168ecfeee8fa19d4cecdedf784d117c95c63d88ddd4c69e32f13
  title: FIBO source MD/DerivativesTemporal/ETOptionsTemporal.rdf
title: options vega
type: Ontology Class
---

# options vega

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionsVega>

## Definition

A measure of the rate of change in an option's theoretical value for a one-unit change in the volatility assumption. Action: add terms that define or influence this.

## Relationships

- **Subclass of**: [OptionsGreek](/concepts/fibo/MD/DerivativesTemporal/ETOptionsTemporal/OptionsGreek.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [OptionTheoreticalValue](/concepts/fibo/MD/DerivativesTemporal/ETOptionsTemporal/OptionTheoreticalValue.md)

## Annotations

- **label** (en): options vega
- **definition** (en): A measure of the rate of change in an option's theoretical value for a one-unit change in the volatility assumption. Action: add terms that define or influence this.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
