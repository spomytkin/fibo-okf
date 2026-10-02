---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unsecured bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond that is only secured by the bond issuer's good credit standing
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Most unsecured bonds pose limited risk of default, as the organizations that issue them are typically financially
      sound.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: debenture
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UnsecuredBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: unsecured bond
type: Ontology Class
---

# unsecured bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UnsecuredBond>

## Definition

bond that is only secured by the bond issuer's good credit standing

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Annotations

- **label**: unsecured bond
- **definition**: bond that is only secured by the bond issuer's good credit standing
- **explanatoryNote**: Most unsecured bonds pose limited risk of default, as the organizations that issue them are typically financially sound.
- **synonym**: debenture

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
