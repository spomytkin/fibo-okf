---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: change action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action to disseminate information regarding a change further described in the corporate action details
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Generic changes may include a change in the terms of an issue, change in the identification of a security, change
      of board lot, change from global to definitive, etc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ChangeAction
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: change action
type: Ontology Class
---

# change action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ChangeAction>

## Definition

corporate action to disseminate information regarding a change further described in the corporate action details

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Annotations

- **label** (en): change action
- **definition** (en): corporate action to disseminate information regarding a change further described in the corporate action details
- **explanatoryNote** (en): Generic changes may include a change in the terms of an issue, change in the identification of a security, change of board lot, change from global to definitive, etc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
