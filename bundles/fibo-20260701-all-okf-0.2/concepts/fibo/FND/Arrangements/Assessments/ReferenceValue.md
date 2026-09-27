---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reference value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: value for something discernible for which evidence can be obtained
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Derivatives, such as certain exotics, can be based on values ascribed to virtually anything, including weather.
      Typically, however, a reference value refers to something that can be readily observed in the marketplace, such as a
      quoted rate (e.g., interest rate, exchange rate), index value, commodity price, stock price, economic indicator, or
      something similar as of some point in time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/QuantitativeValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/QuantitativeValue
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Reference
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ReferenceValue
sources:
- id: fibo-source-eb1f5d06cc
  resource: references/fibo/FND/Arrangements/Assessments.rdf
  sha256: eb1f5d06ccbc0219cb924563f264d0880520c4f7d39ebe73e07d76ad440c2913
  title: FIBO source FND/Arrangements/Assessments.rdf
title: reference value
type: Ontology Class
---

# reference value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ReferenceValue>

## Definition

value for something discernible for which evidence can be obtained

## Relationships

- **Subclass of**: [QuantitativeValue](/concepts/fibo/FND/Arrangements/Assessments/QuantitativeValue.md)
- **Subclass of**: [Reference](<https://www.omg.org/spec/Commons/Documents/Reference>)

## Annotations

- **label**: reference value
- **definition**: value for something discernible for which evidence can be obtained
- **explanatoryNote**: Derivatives, such as certain exotics, can be based on values ascribed to virtually anything, including weather. Typically, however, a reference value refers to something that can be readily observed in the marketplace, such as a quoted rate (e.g., interest rate, exchange rate), index value, commodity price, stock price, economic indicator, or something similar as of some point in time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
