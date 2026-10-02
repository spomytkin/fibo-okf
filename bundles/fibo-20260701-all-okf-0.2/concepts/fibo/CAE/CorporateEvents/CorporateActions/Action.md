---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event announced, initiated or carried out by an organization that affects a legal entity or the securities it issues
      and may have a material impact on that entity's stakeholders, such as shareholders and creditors
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Actions that impact an entity may be initiated by an issuer, exchange, regulator, creditor, or other third party.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Actions initiated by an issuer are typically approved by that company's board of directors and authorized by their
      shareholders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
    value: N9ab935f3ad6941b8bd6355da95963fcb
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/Action
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: action
type: Ontology Class
---

# action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/Action>

## Definition

event announced, initiated or carried out by an organization that affects a legal entity or the securities it issues and may have a material impact on that entity's stakeholders, such as shareholders and creditors

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [ActionClassifier](/concepts/fibo/CAE/CorporateEvents/CorporateActions/ActionClassifier.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from value `N9ab935f3ad6941b8bd6355da95963fcb`

## Annotations

- **label** (en): action
- **definition** (en): event announced, initiated or carried out by an organization that affects a legal entity or the securities it issues and may have a material impact on that entity's stakeholders, such as shareholders and creditors
- **example** (en): Actions that impact an entity may be initiated by an issuer, exchange, regulator, creditor, or other third party.
- **explanatoryNote** (en): Actions initiated by an issuer are typically approved by that company's board of directors and authorized by their shareholders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
