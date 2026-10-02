---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: shares premium dividend action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that pays shareholders an amount in cash issued from the shares premium reserve
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: It is similar to a dividend but with different tax implications.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/SharesPremiumDividendAction
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: shares premium dividend action
type: Ontology Class
---

# shares premium dividend action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/SharesPremiumDividendAction>

## Definition

corporate action that pays shareholders an amount in cash issued from the shares premium reserve

## Relationships

- **Subclass of**: [MandatoryWithChoiceCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryWithChoiceCorporateAction.md)

## Annotations

- **label** (en): shares premium dividend action
- **definition** (en): corporate action that pays shareholders an amount in cash issued from the shares premium reserve
- **explanatoryNote** (en): It is similar to a dividend but with different tax implications.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
