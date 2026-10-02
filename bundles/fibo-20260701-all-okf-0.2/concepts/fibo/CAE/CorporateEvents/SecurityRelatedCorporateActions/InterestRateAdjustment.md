---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate adjustment
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Scheduled change to the coupon rate for a floating or adjustable rate security.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The SWIFT definition as given defines the notification of the interest rate change, not the adjustment. Adjusted
      to describe the event. REVIEW: Is this really an action? Usually consider that it''s expected. Given definition was
      for the announcement. SWIFT full definition "Announcement of the current coupon rate for a floating or adjustable rate
      security."'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponBond
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/InterestRateAdjustment
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: interest rate adjustment
type: Ontology Class
---

# interest rate adjustment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/InterestRateAdjustment>

## Definition

Scheduled change to the coupon rate for a floating or adjustable rate security.

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [VariableCouponBond](/concepts/fibo/SEC/Debt/Bonds/VariableCouponBond.md)

## Annotations

- **label** (en): interest rate adjustment
- **definition** (en): Scheduled change to the coupon rate for a floating or adjustable rate security.
- **explanatoryNote** (en): The SWIFT definition as given defines the notification of the interest rate change, not the adjustment. Adjusted to describe the event. REVIEW: Is this really an action? Usually consider that it's expected. Given definition was for the announcement. SWIFT full definition "Announcement of the current coupon rate for a floating or adjustable rate security."

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
