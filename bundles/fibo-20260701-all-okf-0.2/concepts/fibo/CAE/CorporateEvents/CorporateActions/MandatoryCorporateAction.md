---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mandatory corporate action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: action initiated by the board of directors of a corporation that affects all shareholders
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples of mandatory corporate actions include cash dividends, stock splits, mergers, pre-refunding, return of
      capital, bonus issue, asset ID change, and spin-offs.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Mandatory means mandatory participation by all shareholders, however the shareholder is not required to do anything.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: mandatory corporate action
type: Ontology Class
---

# mandatory corporate action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction>

## Definition

action initiated by the board of directors of a corporation that affects all shareholders

## Relationships

- **Subclass of**: [CorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md)

## Annotations

- **label** (en): mandatory corporate action
- **definition** (en): action initiated by the board of directors of a corporation that affects all shareholders
- **example** (en): Examples of mandatory corporate actions include cash dividends, stock splits, mergers, pre-refunding, return of capital, bonus issue, asset ID change, and spin-offs.
- **explanatoryNote** (en): Mandatory means mandatory participation by all shareholders, however the shareholder is not required to do anything.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
