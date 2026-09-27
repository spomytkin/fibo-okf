---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that permits the holder to acquire a specified amount of a debt instrument or related debt observable a
      specified period at a specified price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/DebtInstrumentDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/DebtInstrumentDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/DebtWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: debt warrant
type: Ontology Class
---

# debt warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/DebtWarrant>

## Definition

warrant that permits the holder to acquire a specified amount of a debt instrument or related debt observable a specified period at a specified price

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)
- **Subclass of**: [DebtInstrumentDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/DebtInstrumentDerivative.md)

## Annotations

- **label** (en): debt warrant
- **definition** (en): warrant that permits the holder to acquire a specified amount of a debt instrument or related debt observable a specified period at a specified price
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
