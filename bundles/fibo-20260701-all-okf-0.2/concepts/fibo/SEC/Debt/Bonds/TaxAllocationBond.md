---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tax allocation bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond payable from the incremental increase in tax revenues realized from any increase in property value and other
      economic activity, often designed to capture the economic benefit resulting from a bond financing
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Tax increment bonds, also known as tax allocation bonds, often are used to finance the redevelopment of blighted
      areas.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/SecuredBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SecuredBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TaxAllocationBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: tax allocation bond
type: Ontology Class
---

# tax allocation bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TaxAllocationBond>

## Definition

bond payable from the incremental increase in tax revenues realized from any increase in property value and other economic activity, often designed to capture the economic benefit resulting from a bond financing

## Relationships

- **Subclass of**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)
- **Subclass of**: [SecuredBond](/concepts/fibo/SEC/Debt/Bonds/SecuredBond.md)

## Annotations

- **label**: tax allocation bond
- **definition**: bond payable from the incremental increase in tax revenues realized from any increase in property value and other economic activity, often designed to capture the economic benefit resulting from a bond financing
- **explanatoryNote**: Tax increment bonds, also known as tax allocation bonds, often are used to finance the redevelopment of blighted areas.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
