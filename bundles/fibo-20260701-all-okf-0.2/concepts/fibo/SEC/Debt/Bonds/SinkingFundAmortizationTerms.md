---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sinking fund amortization terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms for the paydown of principal in a sinking fund type of amortizing security
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: At present there is only a schedule, there should be other terms for what happens on the scheduled dates. Sinking
      fund may be bullet e.g. x percent over year for y years. SF may be mandatory or contingent on some other economic event.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isMandatory
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondAmortizationPaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SinkingFundAmortizationTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: sinking fund amortization terms
type: Ontology Class
---

# sinking fund amortization terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SinkingFundAmortizationTerms>

## Definition

terms for the paydown of principal in a sinking fund type of amortizing security

## Relationships

- **Subclass of**: [BondAmortizationPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)

## Constraints

- **[isMandatory](/concepts/fibo/SEC/Debt/Bonds/isMandatory.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: sinking fund amortization terms
- **definition**: terms for the paydown of principal in a sinking fund type of amortizing security
- **editorialNote**: At present there is only a schedule, there should be other terms for what happens on the scheduled dates. Sinking fund may be bullet e.g. x percent over year for y years. SF may be mandatory or contingent on some other economic event.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
