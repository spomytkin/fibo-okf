---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variance
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of spread, calculated as the average squared deviation of each number from the mean of a data set
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/edu/power-pouvoir/glossary-glossaire/5214842-eng.htm#v
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/symbol
    value: μ2
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/symbol
    value: σ2
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: second moment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Mean
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Dispersion.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Dispersion
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Variance
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: variance
type: Ontology Class
---

# variance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Variance>

## Definition

measure of spread, calculated as the average squared deviation of each number from the mean of a data set

## Relationships

- **Subclass of**: [Dispersion](/concepts/fibo/FND/Utilities/Analytics/Dispersion.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [Mean](/concepts/fibo/FND/Utilities/Analytics/Mean.md)

## Annotations

- **label**: variance
- **definition**: measure of spread, calculated as the average squared deviation of each number from the mean of a data set
- **adaptedFrom**: http://www.statcan.gc.ca/edu/power-pouvoir/glossary-glossaire/5214842-eng.htm#v
- **symbol**: μ2
- **symbol**: σ2
- **synonym**: second moment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
