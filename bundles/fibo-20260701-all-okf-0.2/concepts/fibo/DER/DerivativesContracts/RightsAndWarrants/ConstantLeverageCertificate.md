---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: constant leverage certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entitlement that combines the structure of an open-end certificate with a leverage option with no fixed term, making
      leverage available without a term restriction, without a knock-out barrier dependency
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/ConstantLeverageCertificate
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: constant leverage certificate
type: Ontology Class
---

# constant leverage certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/ConstantLeverageCertificate>

## Definition

entitlement that combines the structure of an open-end certificate with a leverage option with no fixed term, making leverage available without a term restriction, without a knock-out barrier dependency

## Relationships

- **Subclass of**: [SecurityBasedDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md)
- **Subclass of**: [Entitlement](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)
- **Subclass of**: [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)

## Annotations

- **label** (en): constant leverage certificate
- **definition** (en): entitlement that combines the structure of an open-end certificate with a leverage option with no fixed term, making leverage available without a term restriction, without a knock-out barrier dependency
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
