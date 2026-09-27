---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: allotment right formula
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rule applied to calculate the number of securities for an allotment right, typically based on the number of these
      instruments that the holder holds
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that there may be a combination of a rule expressed in text as well as an expression or more complex formula
      embedded in a contract for making this determination.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/AllotmentRightFormula
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: allotment right formula
type: Ontology Class
---

# allotment right formula

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/AllotmentRightFormula>

## Definition

rule applied to calculate the number of securities for an allotment right, typically based on the number of these instruments that the holder holds

## Relationships

- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Annotations

- **label** (en): allotment right formula
- **definition** (en): rule applied to calculate the number of securities for an allotment right, typically based on the number of these instruments that the holder holds
- **explanatoryNote** (en): Note that there may be a combination of a rule expressed in text as well as an expression or more complex formula embedded in a contract for making this determination.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
