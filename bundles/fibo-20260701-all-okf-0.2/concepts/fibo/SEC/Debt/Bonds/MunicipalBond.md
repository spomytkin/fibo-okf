---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: municipal bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: government bond that may be issued by a regional, rather than national, authority
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: muni
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Municipal bonds may be issued by states, cities, counties, special tax districts or special agencies or authorities
      of state or local governments.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: municipal bond
type: Ontology Class
---

# municipal bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond>

## Definition

government bond that may be issued by a regional, rather than national, authority

## Relationships

- **Subclass of**: [GovernmentBond](/concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md)
- **Subclass of**: [MunicipalSecurity](/concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md)

## Annotations

- **label**: municipal bond
- **definition**: government bond that may be issued by a regional, rather than national, authority
- **abbreviation**: muni
- **explanatoryNote**: Municipal bonds may be issued by states, cities, counties, special tax districts or special agencies or authorities of state or local governments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
