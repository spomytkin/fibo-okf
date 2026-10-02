---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has municipal trustee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the financial institution with trust powers, designated by the issuer, that acts, pursuant to a bond
      contract, in a fiduciary capacity for the benefit of the bondholders in enforcing the terms of the bond contract
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  range:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalTrustee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalTrustee
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasMunicipalTrustee
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has municipal trustee
type: Ontology Property
---

# has municipal trustee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasMunicipalTrustee>

## Definition

specifies the financial institution with trust powers, designated by the issuer, that acts, pursuant to a bond contract, in a fiduciary capacity for the benefit of the bondholders in enforcing the terms of the bond contract

## Relationships

- **Domain**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)
- **Range**: [MunicipalTrustee](/concepts/fibo/SEC/Debt/Bonds/MunicipalTrustee.md)
- **Subproperty of**: [hasThirdParty](/concepts/fibo/FND/Agreements/Contracts/hasThirdParty.md)

## Annotations

- **label**: has municipal trustee
- **definition**: specifies the financial institution with trust powers, designated by the issuer, that acts, pursuant to a bond contract, in a fiduciary capacity for the benefit of the bondholders in enforcing the terms of the bond contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
