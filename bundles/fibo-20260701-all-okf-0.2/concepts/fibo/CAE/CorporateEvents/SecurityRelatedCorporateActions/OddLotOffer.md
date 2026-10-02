---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: odd lot offer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Offer by issuer to allow holders of an odd lot of a security to order a commission-free transaction at market price,
      to sell the odd lot, or to buy an amount of shares which will bring the position to a round lot (board lot). SWIFT =
      ODLT
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/OddLotOffer
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: odd lot offer
type: Ontology Class
---

# odd lot offer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/OddLotOffer>

## Definition

Offer by issuer to allow holders of an odd lot of a security to order a commission-free transaction at market price, to sell the odd lot, or to buy an amount of shares which will bring the position to a round lot (board lot). SWIFT = ODLT

## Relationships

- **Subclass of**: [VoluntaryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)

## Annotations

- **label** (en): odd lot offer
- **definition** (en): Offer by issuer to allow holders of an odd lot of a security to order a commission-free transaction at market price, to sell the odd lot, or to buy an amount of shares which will bring the position to a round lot (board lot). SWIFT = ODLT

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
