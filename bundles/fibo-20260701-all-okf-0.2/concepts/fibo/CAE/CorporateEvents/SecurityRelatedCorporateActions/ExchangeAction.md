---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exchange action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that reflects an exchange of holdings for other securities and/or cash
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The exchange can be either mandatory or voluntary involving the exchange of outstanding securities for different
      securities and/or cash. For example, 'exchange offer', 'capital reorganisation' or 'funds separation'.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/ExchangeAction
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: exchange action
type: Ontology Class
---

# exchange action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/ExchangeAction>

## Definition

corporate action that reflects an exchange of holdings for other securities and/or cash

## Relationships

- **Subclass of**: [CorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md)

## Annotations

- **label** (en): exchange action
- **definition** (en): corporate action that reflects an exchange of holdings for other securities and/or cash
- **explanatoryNote** (en): The exchange can be either mandatory or voluntary involving the exchange of outstanding securities for different securities and/or cash. For example, 'exchange offer', 'capital reorganisation' or 'funds separation'.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
