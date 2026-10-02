---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: general obligation municipal bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: municipal bond that is backed by the full faith and credit and general resources of the issuing municipality, including
      its general taxing authority
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: GO bond
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/RevenueBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RevenueBond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/FullFaithCreditBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FullFaithCreditBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GeneralObligationMunicipalBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: general obligation municipal bond
type: Ontology Class
---

# general obligation municipal bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GeneralObligationMunicipalBond>

## Definition

municipal bond that is backed by the full faith and credit and general resources of the issuing municipality, including its general taxing authority

## Relationships

- **Subclass of**: [FullFaithCreditBond](/concepts/fibo/SEC/Debt/Bonds/FullFaithCreditBond.md)
- **Subclass of**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)

## Constraints

- **Disjoint with**: [RevenueBond](/concepts/fibo/SEC/Debt/Bonds/RevenueBond.md)

## Annotations

- **label**: general obligation municipal bond
- **definition**: municipal bond that is backed by the full faith and credit and general resources of the issuing municipality, including its general taxing authority
- **abbreviation**: GO bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
