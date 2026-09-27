---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: voluntary corporate action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event in which the shareholders elect to participate and must respond in order for the issuer to process the action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: An example of a voluntary corporate action is a tender offer, in which the issuer may request shareholders to tender
      their shares at a predetermined price.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Shareholders send responses to the issuer's agents, and the issuer will send the proceeds of the action to those
      shareholders who elect to participate.
  disjoint_with:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: voluntary corporate action
type: Ontology Class
---

# voluntary corporate action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction>

## Definition

event in which the shareholders elect to participate and must respond in order for the issuer to process the action

## Relationships

- **Subclass of**: [CorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md)

## Constraints

- **Disjoint with**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Annotations

- **label** (en): voluntary corporate action
- **definition** (en): event in which the shareholders elect to participate and must respond in order for the issuer to process the action
- **example** (en): An example of a voluntary corporate action is a tender offer, in which the issuer may request shareholders to tender their shares at a predetermined price.
- **explanatoryNote** (en): Shareholders send responses to the issuer's agents, and the issuer will send the proceeds of the action to those shareholders who elect to participate.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
