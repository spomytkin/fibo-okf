---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: municipal trustee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution with trust powers, designated by the issuer, that acts, pursuant to a bond contract, in a
      fiduciary capacity for the benefit of the bondholders in enforcing the terms of the bond contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In many cases, the trustee also acts as custodian, paying agent, registrar and/or transfer agent for the bonds.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/Trusts/Trusts/Trustee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustee
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalTrustee
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: municipal trustee
type: Ontology Class
---

# municipal trustee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalTrustee>

## Definition

financial institution with trust powers, designated by the issuer, that acts, pursuant to a bond contract, in a fiduciary capacity for the benefit of the bondholders in enforcing the terms of the bond contract

## Relationships

- **Subclass of**: [Trustee](/concepts/fibo/BE/Trusts/Trusts/Trustee.md)
- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label**: municipal trustee
- **definition**: financial institution with trust powers, designated by the issuer, that acts, pursuant to a bond contract, in a fiduciary capacity for the benefit of the bondholders in enforcing the terms of the bond contract
- **explanatoryNote**: In many cases, the trustee also acts as custodian, paying agent, registrar and/or transfer agent for the bonds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
