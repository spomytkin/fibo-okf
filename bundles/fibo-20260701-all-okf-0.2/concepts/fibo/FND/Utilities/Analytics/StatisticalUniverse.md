---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statistical universe
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection representing the total membership, or 'universe', of people, resources, products, services, events,
      or entities of interest for some question, experiment, survey or statistical program
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: A statistical universe can be a group of actually existing objects (e.g. the set of all stars within the Milky
      Way galaxy) or a hypothetical and potentially infinite group of objects conceived as a generalization from experience
      (e.g. the set of all possible hands in a game of poker).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: http://stats.oecd.org/glossary/detail.asp?ID=2087
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasUniverseSize
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalProgram
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalUniverse
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: statistical universe
type: Ontology Class
---

# statistical universe

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalUniverse>

## Definition

collection representing the total membership, or 'universe', of people, resources, products, services, events, or entities of interest for some question, experiment, survey or statistical program

## Relationships

- **Related to**: [detail.asp](<http://stats.oecd.org/glossary/detail.asp?ID=2087>)
- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[hasUniverseSize](/concepts/fibo/FND/Utilities/Analytics/hasUniverseSize.md)**: all values from of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [StatisticalProgram](/concepts/fibo/FND/Utilities/Analytics/StatisticalProgram.md)

## Annotations

- **label**: statistical universe
- **definition**: collection representing the total membership, or 'universe', of people, resources, products, services, events, or entities of interest for some question, experiment, survey or statistical program
- **example**: A statistical universe can be a group of actually existing objects (e.g. the set of all stars within the Milky Way galaxy) or a hypothetical and potentially infinite group of objects conceived as a generalization from experience (e.g. the set of all possible hands in a game of poker).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
