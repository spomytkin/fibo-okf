---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: income-oriented classifier
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier of corporate actions that impacts income to shareholders
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Cash dividends are a classic example where a public company declares a dividend to be paid on each outstanding
      share. Bonus is another case where the shareholder is rewarded. In a stricter sense, the bonus issue should not impact
      the share price but in reality, in rare cases, it does and results in an overall increase in value.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/ActionClassifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/IncomeOrientedClassifier
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: income-oriented classifier
type: Ontology Class
---

# income-oriented classifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/IncomeOrientedClassifier>

## Definition

classifier of corporate actions that impacts income to shareholders

## Relationships

- **Subclass of**: [ActionClassifier](/concepts/fibo/CAE/CorporateEvents/CorporateActions/ActionClassifier.md)

## Annotations

- **label** (en): income-oriented classifier
- **definition** (en): classifier of corporate actions that impacts income to shareholders
- **explanatoryNote** (en): Cash dividends are a classic example where a public company declares a dividend to be paid on each outstanding share. Bonus is another case where the shareholder is rewarded. In a stricter sense, the bonus issue should not impact the share price but in reality, in rare cases, it does and results in an overall increase in value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
