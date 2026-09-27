---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: cash dividend action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that distributes cash to shareholders in proportion to their equity holding
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Ordinary dividends are typically recurring and regular. The shareholder must take cash, and may be offered a choice
      of currency.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CashDividendAction
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: cash dividend action
type: Ontology Class
---

# cash dividend action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CashDividendAction>

## Definition

corporate action that distributes cash to shareholders in proportion to their equity holding

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Annotations

- **label** (en): cash dividend action
- **definition** (en): corporate action that distributes cash to shareholders in proportion to their equity holding
- **explanatoryNote** (en): Ordinary dividends are typically recurring and regular. The shareholder must take cash, and may be offered a choice of currency.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
