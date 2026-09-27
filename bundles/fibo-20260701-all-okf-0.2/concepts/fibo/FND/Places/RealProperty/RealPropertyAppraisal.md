---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: real property appraisal
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: value assessment that estimates the amount of money some real property is worth
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The valuation uses one or more methodologies and is conducted by an appraiser or technology with a logical model
      that performs the same function.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PropertyInspectionReport
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraiser
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/Appraisal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealPropertyAppraisal
sources:
- id: fibo-source-f0e5ecd06c
  resource: references/fibo/FND/Places/RealProperty.rdf
  sha256: f0e5ecd06c164d1e5fff0c1236869b2014bcba3d7008365dcc2c7363064202bd
  title: FIBO source FND/Places/RealProperty.rdf
title: real property appraisal
type: Ontology Class
---

# real property appraisal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealPropertyAppraisal>

## Definition

value assessment that estimates the amount of money some real property is worth

## Relationships

- **Subclass of**: [Appraisal](/concepts/fibo/FND/Arrangements/Assessments/Appraisal.md)

## Constraints

- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: min qualified cardinality 0 of type [PropertyInspectionReport](/concepts/fibo/FND/Places/RealProperty/PropertyInspectionReport.md)
- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: some values from of type [RealProperty](/concepts/fibo/FND/Places/RealProperty/RealProperty.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [Appraiser](/concepts/fibo/FND/Arrangements/Assessments/Appraiser.md)

## Annotations

- **label**: real property appraisal
- **definition**: value assessment that estimates the amount of money some real property is worth
- **explanatoryNote**: The valuation uses one or more methodologies and is conducted by an appraiser or technology with a logical model that performs the same function.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
