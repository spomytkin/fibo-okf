---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: action group
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier that differentiates corporate actions based on a GLEIF specific grouping
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/Action
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals/ActionGroup
sources:
- id: fibo-source-7606bb41f7
  resource: references/fibo/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals.rdf
  sha256: 7606bb41f72dc98e8e5f1d4b5c970686f1a3473c0e6baee42ec320289773c087
  title: FIBO source CAE/CorporateEvents/GLEIF-CorporateActionIndividuals.rdf
title: action group
type: Ontology Class
---

# action group

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/GLEIF-CorporateActionIndividuals/ActionGroup>

## Definition

classifier that differentiates corporate actions based on a GLEIF specific grouping

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Action](/concepts/fibo/CAE/CorporateEvents/CorporateActions/Action.md)
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): action group
- **definition** (en): classifier that differentiates corporate actions based on a GLEIF specific grouping

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
