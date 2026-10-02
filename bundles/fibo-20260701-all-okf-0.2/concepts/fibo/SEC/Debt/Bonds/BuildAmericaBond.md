---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Build America Bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: taxable municipal bond issued through December 31, 2010 under the American Recovery and Reinvestment Act of 2009
      (ARRA)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: BABs may be direct pay subsidy bonds or tax credit bonds.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BuildAmericaBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: Build America Bond
type: Ontology Class
---

# Build America Bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BuildAmericaBond>

## Definition

taxable municipal bond issued through December 31, 2010 under the American Recovery and Reinvestment Act of 2009 (ARRA)

## Relationships

- **Subclass of**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)

## Annotations

- **label**: Build America Bond
- **definition**: taxable municipal bond issued through December 31, 2010 under the American Recovery and Reinvestment Act of 2009 (ARRA)
- **explanatoryNote**: BABs may be direct pay subsidy bonds or tax credit bonds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
