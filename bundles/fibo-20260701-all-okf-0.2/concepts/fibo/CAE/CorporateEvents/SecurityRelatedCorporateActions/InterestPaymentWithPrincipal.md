---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest payment with principal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A payment of a portion of the principal of an interest bearing asset, in addition to the interest payment. SWIFT
      = PRII
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions/InterestPaymentAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/InterestPaymentAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/InterestPaymentWithPrincipal
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: interest payment with principal
type: Ontology Class
---

# interest payment with principal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/InterestPaymentWithPrincipal>

## Definition

A payment of a portion of the principal of an interest bearing asset, in addition to the interest payment. SWIFT = PRII

## Relationships

- **Subclass of**: [InterestPaymentAction](/concepts/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions/InterestPaymentAction.md)

## Annotations

- **label** (en): interest payment with principal
- **definition** (en): A payment of a portion of the principal of an interest bearing asset, in addition to the interest payment. SWIFT = PRII

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
