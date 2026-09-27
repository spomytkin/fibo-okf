---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: put warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant giving the buyer (holder) the right, but not the obligation, to sell the assets specified (i.e., acquire
      cash in exchange for the underlying assets, such as stock) back to the issuer at a fixed price or formula, on or before
      a specified date
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A put warrant is essentially a company-issued option to sell shares back to the issuer.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PutWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: put warrant
type: Ontology Class
---

# put warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PutWarrant>

## Definition

warrant giving the buyer (holder) the right, but not the obligation, to sell the assets specified (i.e., acquire cash in exchange for the underlying assets, such as stock) back to the issuer at a fixed price or formula, on or before a specified date

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Annotations

- **label** (en): put warrant
- **definition** (en): warrant giving the buyer (holder) the right, but not the obligation, to sell the assets specified (i.e., acquire cash in exchange for the underlying assets, such as stock) back to the issuer at a fixed price or formula, on or before a specified date
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): A put warrant is essentially a company-issued option to sell shares back to the issuer.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
