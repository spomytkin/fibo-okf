---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: finite population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: population for which it is possible to count its units
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=3649
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In statistics, a population is a set of similar items or events of interest for some question or experiment. In
      other words, a population is the complete group of units to which survey results are to apply. (These units may be persons,
      animals, objects, businesses, trips, etc.). See http://www.statcan.gc.ca/edu/power-pouvoir/glossary-glossaire/5214842-eng.htm#p.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/FinitePopulation
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: finite population
type: Ontology Class
---

# finite population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/FinitePopulation>

## Definition

population for which it is possible to count its units

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Annotations

- **label**: finite population
- **definition**: population for which it is possible to count its units
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=3649
- **explanatoryNote**: In statistics, a population is a set of similar items or events of interest for some question or experiment. In other words, a population is the complete group of units to which survey results are to apply. (These units may be persons, animals, objects, businesses, trips, etc.). See http://www.statcan.gc.ca/edu/power-pouvoir/glossary-glossaire/5214842-eng.htm#p.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
