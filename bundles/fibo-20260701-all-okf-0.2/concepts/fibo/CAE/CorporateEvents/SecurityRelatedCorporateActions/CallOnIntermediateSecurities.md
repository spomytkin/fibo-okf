---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: call on intermediate securities
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that involves a call or exercise on nil paid securities or intermediate securities resulting from
      an intermediate securities distribution (RHDI)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This code is used for the second event, when an intermediate securities' issue (rights/coupons) is composed of
      two events, the first event being the distribution of intermediate securities.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CallOnIntermediateSecurities
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: call on intermediate securities
type: Ontology Class
---

# call on intermediate securities

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CallOnIntermediateSecurities>

## Definition

corporate action that involves a call or exercise on nil paid securities or intermediate securities resulting from an intermediate securities distribution (RHDI)

## Relationships

- **Subclass of**: [MandatoryWithChoiceCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction.md)

## Annotations

- **label** (en): call on intermediate securities
- **definition** (en): corporate action that involves a call or exercise on nil paid securities or intermediate securities resulting from an intermediate securities distribution (RHDI)
- **explanatoryNote** (en): This code is used for the second event, when an intermediate securities' issue (rights/coupons) is composed of two events, the first event being the distribution of intermediate securities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
