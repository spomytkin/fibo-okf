---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rights exercise event
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Exercising the right to purchase the shares. Furhter Notes: This is an action on the part of the holder. SWIFT:
      Call/exercise on nil-paid securities/rights resulting from a rights distribution (RHDI) (To be used for the second event
      in case rights issue is dealt with in 2 events, first event being the RHDI).'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There is a rights trading period overlaps with rights subscriptiuon period (you can trade the rights) Rights exercise
      period - expiry date. Some time after the expiry the new shares are distributed. This is the distribution.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/RightsExerciseEvent
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: rights exercise event
type: Ontology Class
---

# rights exercise event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/RightsExerciseEvent>

## Definition

Exercising the right to purchase the shares. Furhter Notes: This is an action on the part of the holder. SWIFT: Call/exercise on nil-paid securities/rights resulting from a rights distribution (RHDI) (To be used for the second event in case rights issue is dealt with in 2 events, first event being the RHDI).

## Relationships

- **Subclass of**: [CorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md)

## Annotations

- **label** (en): rights exercise event
- **definition** (en): Exercising the right to purchase the shares. Furhter Notes: This is an action on the part of the holder. SWIFT: Call/exercise on nil-paid securities/rights resulting from a rights distribution (RHDI) (To be used for the second event in case rights issue is dealt with in 2 events, first event being the RHDI).
- **explanatoryNote** (en): There is a rights trading period overlaps with rights subscriptiuon period (you can trade the rights) Rights exercise period - expiry date. Some time after the expiry the new shares are distributed. This is the distribution.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
