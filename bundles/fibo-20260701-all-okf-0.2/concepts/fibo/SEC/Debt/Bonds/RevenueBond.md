---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: revenue bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: municipal bond supported by the revenue from a specific project
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Revenue bonds are municipal bonds that finance income-producing projects, such as toll bridges, highways, or local
      stadiums, and are secured by a specified revenue source. Typically, revenue bonds can be issued by any government agency
      or fund that is managed in the manner of a business, such as entities having both operating revenues and expenses.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/SecuredBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SecuredBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RevenueBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: revenue bond
type: Ontology Class
---

# revenue bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RevenueBond>

## Definition

municipal bond supported by the revenue from a specific project

## Relationships

- **Subclass of**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)
- **Subclass of**: [SecuredBond](/concepts/fibo/SEC/Debt/Bonds/SecuredBond.md)

## Annotations

- **label**: revenue bond
- **definition**: municipal bond supported by the revenue from a specific project
- **explanatoryNote**: Revenue bonds are municipal bonds that finance income-producing projects, such as toll bridges, highways, or local stadiums, and are secured by a specified revenue source. Typically, revenue bonds can be issued by any government agency or fund that is managed in the manner of a business, such as entities having both operating revenues and expenses.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
