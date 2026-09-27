---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: action classifier
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier that distinguishes the kinds of actions and events that may be announced, initiated or carried out by
      an organization that affects a legal entity or the securities it issues, such as income-oriented events
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: ISO 15022 classifies events as impacting income vs. others. Other classification schemes distinguish between actions
      that return profits to shareholders, actions that are designed to influence the share price, and actions involving a
      change in structure to the issuer organization.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/Action
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassifier
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: action classifier
type: Ontology Class
---

# action classifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassifier>

## Definition

classifier that distinguishes the kinds of actions and events that may be announced, initiated or carried out by an organization that affects a legal entity or the securities it issues, such as income-oriented events

## Relationships

- **Subclass of**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Action](/concepts/fibo/CAE/CorporateEvents/CorporateActions/Action.md)
- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: exact qualified cardinality 1 of type [ActionClassificationScheme](/concepts/fibo/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme.md)
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [ActionClassificationScheme](/concepts/fibo/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme.md)

## Annotations

- **label** (en): action classifier
- **definition** (en): classifier that distinguishes the kinds of actions and events that may be announced, initiated or carried out by an organization that affects a legal entity or the securities it issues, such as income-oriented events
- **explanatoryNote** (en): ISO 15022 classifies events as impacting income vs. others. Other classification schemes distinguish between actions that return profits to shareholders, actions that are designed to influence the share price, and actions involving a change in structure to the issuer organization.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
