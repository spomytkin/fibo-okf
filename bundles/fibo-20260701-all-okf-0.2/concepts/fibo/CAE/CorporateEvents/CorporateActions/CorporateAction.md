---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: corporate action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: action carried out by or specifically relating to a legal entity that may affect the securities it issues and may
      have a material impact on its stakeholders, such as shareholders and creditors
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples of corporate actions include share issues, stock splits, consolidation, dividends, mergers and acquisitions,
      rights issues, spin-offs, and the inception of court actions.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Corporate actions are typically approved by a company's board of directors and authorized by the shareholders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/Action.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/Action
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: corporate action
type: Ontology Class
---

# corporate action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction>

## Definition

action carried out by or specifically relating to a legal entity that may affect the securities it issues and may have a material impact on its stakeholders, such as shareholders and creditors

## Relationships

- **Subclass of**: [Action](/concepts/fibo/CAE/CorporateEvents/CorporateActions/Action.md)

## Annotations

- **label** (en): corporate action
- **definition** (en): action carried out by or specifically relating to a legal entity that may affect the securities it issues and may have a material impact on its stakeholders, such as shareholders and creditors
- **example** (en): Examples of corporate actions include share issues, stock splits, consolidation, dividends, mergers and acquisitions, rights issues, spin-offs, and the inception of court actions.
- **explanatoryNote** (en): Corporate actions are typically approved by a company's board of directors and authorized by the shareholders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
