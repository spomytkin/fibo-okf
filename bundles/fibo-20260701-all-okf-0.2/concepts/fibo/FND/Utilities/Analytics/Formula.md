---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: formula
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rule expressed in letters and symbols that consists of at least one expression
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: complex expression
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Specification
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Formula
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: formula
type: Ontology Class
---

# formula

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Formula>

## Definition

rule expressed in letters and symbols that consists of at least one expression

## Relationships

- **Subclass of**: [Specification](<https://www.omg.org/spec/Commons/Documents/Specification>)

## Constraints

- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: some values from of type [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Annotations

- **label**: formula
- **definition**: rule expressed in letters and symbols that consists of at least one expression
- **synonym**: complex expression

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
