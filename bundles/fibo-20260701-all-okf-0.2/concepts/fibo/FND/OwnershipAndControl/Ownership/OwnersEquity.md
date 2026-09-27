---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: owners' equity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: owners' share in a business plus operating profit
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Banking Terms, Sixth Edition, 2012.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Owner's equity is represented by capital investments and accumulated earnings less any dividends or other financial
      obligations. It is typically used to talk about equity in a business, but may also refer to the net assets of a pool
      or special purpose vehicle.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: equity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: net worth
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: capital
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: contributed capital
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/PaidInCapital
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/RetainedEarnings
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/OwnersEquity
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: owners' equity
type: Ontology Class
---

# owners' equity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/OwnersEquity>

## Definition

owners' share in a business plus operating profit

## Relationships

- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: min qualified cardinality 0 of type [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [PaidInCapital](/concepts/fibo/FND/OwnershipAndControl/Ownership/PaidInCapital.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [RetainedEarnings](/concepts/fibo/FND/OwnershipAndControl/Ownership/RetainedEarnings.md)

## Annotations

- **label** (en): owners' equity
- **definition**: owners' share in a business plus operating profit
- **adaptedFrom**: Barron's Dictionary of Banking Terms, Sixth Edition, 2012.
- **explanatoryNote**: Owner's equity is represented by capital investments and accumulated earnings less any dividends or other financial obligations. It is typically used to talk about equity in a business, but may also refer to the net assets of a pool or special purpose vehicle.
- **synonym**: equity
- **synonym**: net worth
- **synonym** (en): capital
- **synonym** (en): contributed capital

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
