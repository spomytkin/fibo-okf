---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has extraordinary redemption provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates the redemption provision of a debt instrument to one-time provision that may be exercised by the issuer
      under certain circumstances
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision
  range:
  - concept: /concepts/fibo/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasExtraordinaryRedemptionProvision
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has extraordinary redemption provision
type: Ontology Property
---

# has extraordinary redemption provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasExtraordinaryRedemptionProvision>

## Definition

relates the redemption provision of a debt instrument to one-time provision that may be exercised by the issuer under certain circumstances

## Relationships

- **Domain**: [RedemptionProvision](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- **Range**: [ExtraordinaryRedemptionProvision](/concepts/fibo/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision.md)
- **Subproperty of**: [hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)

## Annotations

- **label**: has extraordinary redemption provision
- **definition**: relates the redemption provision of a debt instrument to one-time provision that may be exercised by the issuer under certain circumstances

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
