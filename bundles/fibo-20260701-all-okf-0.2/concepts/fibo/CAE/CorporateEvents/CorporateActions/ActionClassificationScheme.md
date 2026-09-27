---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: action classification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: scheme for classifying the kinds of actions and events that may be announced, initiated or carried out by an organization
      that affects a legal entity or the securities it issues
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: The set of corporate actions and income events included herein are a subset of those specified in a combination
      of ISO 15022 Securities - Scheme for Messages (Data Field Dictionary) and the GLEIF LEI-related corporate actions. Other
      schemes that are specific to a custodian, depository, or regulatory agency may also be important, and should take a
      similar approach with respect to classification.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassifier
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: action classification scheme
type: Ontology Class
---

# action classification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme>

## Definition

scheme for classifying the kinds of actions and events that may be announced, initiated or carried out by an organization that affects a legal entity or the securities it issues

## Relationships

- **Subclass of**: [ClassificationScheme](<https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme>)
- **Subclass of**: [CodeSet](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: all values from of type [ActionClassifier](/concepts/fibo/CAE/CorporateEvents/CorporateActions/ActionClassifier.md)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [ActionClassifier](/concepts/fibo/CAE/CorporateEvents/CorporateActions/ActionClassifier.md)

## Annotations

- **label**: action classification scheme
- **definition**: scheme for classifying the kinds of actions and events that may be announced, initiated or carried out by an organization that affects a legal entity or the securities it issues
- **usageNote**: The set of corporate actions and income events included herein are a subset of those specified in a combination of ISO 15022 Securities - Scheme for Messages (Data Field Dictionary) and the GLEIF LEI-related corporate actions. Other schemes that are specific to a custodian, depository, or regulatory agency may also be important, and should take a similar approach with respect to classification.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
