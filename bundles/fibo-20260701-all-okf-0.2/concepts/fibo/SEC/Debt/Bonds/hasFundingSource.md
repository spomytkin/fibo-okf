---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has funding source
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the source of funds for a new issue of municipal securities
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalSecurity
  range:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalDebtSourceOfFunds.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalDebtSourceOfFunds
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/hasDataSource
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFundingSource
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has funding source
type: Ontology Property
---

# has funding source

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFundingSource>

## Definition

indicates the source of funds for a new issue of municipal securities

## Relationships

- **Domain**: [MunicipalSecurity](/concepts/fibo/SEC/Debt/Bonds/MunicipalSecurity.md)
- **Range**: [MunicipalDebtSourceOfFunds](/concepts/fibo/SEC/Debt/Bonds/MunicipalDebtSourceOfFunds.md)
- **Subproperty of**: [hasDataSource](<https://www.omg.org/spec/Commons/Documents/hasDataSource>)

## Annotations

- **label**: has funding source
- **definition**: indicates the source of funds for a new issue of municipal securities

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
