---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: repurchase offer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action in which an offer is made to existing shareholders by the issuing company to repurchase equity
      or other securities convertible into equity
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The objective of the offer is to reduce the number of outstanding equities.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: issuer bid
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: reverse rights
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/RepurchaseOffer
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: repurchase offer
type: Ontology Class
---

# repurchase offer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/RepurchaseOffer>

## Definition

corporate action in which an offer is made to existing shareholders by the issuing company to repurchase equity or other securities convertible into equity

## Relationships

- **Subclass of**: [VoluntaryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)

## Annotations

- **label** (en): repurchase offer
- **definition** (en): corporate action in which an offer is made to existing shareholders by the issuing company to repurchase equity or other securities convertible into equity
- **explanatoryNote** (en): The objective of the offer is to reduce the number of outstanding equities.
- **synonym** (en): issuer bid
- **synonym** (en): reverse rights

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
