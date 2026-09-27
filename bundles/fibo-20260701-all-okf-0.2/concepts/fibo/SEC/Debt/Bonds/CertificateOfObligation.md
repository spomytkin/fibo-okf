---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: certificate of obligation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: municipal security available to governing councils in case of emergency, such as a natural disaster, that needs
      immediate action without time for voter referendum
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CO
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: CO's are similar to GO bonds, except that they do not require voter approval before they are issued. The CO's are
      also guaranteed by the City's taxation power and are counted in the calculation of the tax rate that is needed to support
      debt payments.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For example, when a hurricane destroys the police and emergency services building, there is no time to go through
      the process of voter referendum. The local council must be able to borrow the money to set up provisional buildings
      and necessary equipment for police and emergency services so that the community is served in continuity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CertificateOfObligation
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: certificate of obligation
type: Ontology Class
---

# certificate of obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CertificateOfObligation>

## Definition

municipal security available to governing councils in case of emergency, such as a natural disaster, that needs immediate action without time for voter referendum

## Relationships

- **Subclass of**: [MunicipalSecurity](/concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md)

## Annotations

- **label**: certificate of obligation
- **definition**: municipal security available to governing councils in case of emergency, such as a natural disaster, that needs immediate action without time for voter referendum
- **abbreviation**: CO
- **explanatoryNote**: CO's are similar to GO bonds, except that they do not require voter approval before they are issued. The CO's are also guaranteed by the City's taxation power and are counted in the calculation of the tax rate that is needed to support debt payments.
- **explanatoryNote**: For example, when a hurricane destroys the police and emergency services building, there is no time to go through the process of voter referendum. The local council must be able to borrow the money to set up provisional buildings and necessary equipment for police and emergency services so that the community is served in continuity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
