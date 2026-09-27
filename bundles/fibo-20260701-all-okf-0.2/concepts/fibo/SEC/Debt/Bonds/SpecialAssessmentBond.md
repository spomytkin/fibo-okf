---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: special assessment bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: municipal bond used to fund a development project that is payable from the revenues of an assessment (tax) on the
      community that is intended to benefit from the project
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A special assessment is a charge imposed against a property in a particular locality because that property receives
      a special benefit by virtue of some public improvement, separate and apart from the general benefit accruing to the
      public at large. Special assessments may be apportioned according to the value of the benefit received, rather than
      merely the cost of the improvement.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/SecuredBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SecuredBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SpecialAssessmentBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: special assessment bond
type: Ontology Class
---

# special assessment bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SpecialAssessmentBond>

## Definition

municipal bond used to fund a development project that is payable from the revenues of an assessment (tax) on the community that is intended to benefit from the project

## Relationships

- **Subclass of**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)
- **Subclass of**: [SecuredBond](/concepts/fibo/SEC/Debt/Bonds/SecuredBond.md)

## Annotations

- **label**: special assessment bond
- **definition**: municipal bond used to fund a development project that is payable from the revenues of an assessment (tax) on the community that is intended to benefit from the project
- **explanatoryNote**: A special assessment is a charge imposed against a property in a particular locality because that property receives a special benefit by virtue of some public improvement, separate and apart from the general benefit accruing to the public at large. Special assessments may be apportioned according to the value of the benefit received, rather than merely the cost of the improvement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
