---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sampling variance
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of the extent to which the estimate of a characteristic from different possible samples of the same size
      and the same design differ from one another
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/pub/12-587-x/12-587-x2003001-eng.pdf
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://stats.oecd.org/glossary/detail.asp?ID=3834
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The word 'sampling' can usually be omitted, as being defined by the context or otherwise understood. The sampling
      variance of a statistic is the square of its standard error.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Variance.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Variance
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/SamplingVariance
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: sampling variance
type: Ontology Class
---

# sampling variance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/SamplingVariance>

## Definition

measure of the extent to which the estimate of a characteristic from different possible samples of the same size and the same design differ from one another

## Relationships

- **Subclass of**: [Variance](/concepts/fibo/FND/Utilities/Analytics/Variance.md)

## Annotations

- **label**: sampling variance
- **definition**: measure of the extent to which the estimate of a characteristic from different possible samples of the same size and the same design differ from one another
- **adaptedFrom**: http://www.statcan.gc.ca/pub/12-587-x/12-587-x2003001-eng.pdf
- **adaptedFrom**: https://stats.oecd.org/glossary/detail.asp?ID=3834
- **explanatoryNote**: The word 'sampling' can usually be omitted, as being defined by the context or otherwise understood. The sampling variance of a statistic is the square of its standard error.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
