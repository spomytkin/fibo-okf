---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dividend option action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that involves distribution of a dividend to shareholders with a choice of benefit to receive
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Shareholders may choose to receive shares or cash. A dividend option action is distinguished from reinvestment
      (DRIP) as, like a cash dividend, the company creates new share capital in exchange for the dividend rather than investing
      the dividend in the market.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/DividendOptionAction
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: dividend option action
type: Ontology Class
---

# dividend option action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/DividendOptionAction>

## Definition

corporate action that involves distribution of a dividend to shareholders with a choice of benefit to receive

## Relationships

- **Subclass of**: [MandatoryWithChoiceCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction.md)

## Annotations

- **label** (en): dividend option action
- **definition** (en): corporate action that involves distribution of a dividend to shareholders with a choice of benefit to receive
- **explanatoryNote** (en): Shareholders may choose to receive shares or cash. A dividend option action is distinguished from reinvestment (DRIP) as, like a cash dividend, the company creates new share capital in exchange for the dividend rather than investing the dividend in the market.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
