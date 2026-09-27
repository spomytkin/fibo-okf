---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partial call feature
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: call feature whereby the issuer can recall part of the issue on scheduled dates, where bonds are selected to be
      called according to some rule, or by selecting various bonds at random
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialRedemptionAllocationConvention
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasPartialRedemptionAllocationConvention
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialCallFeature
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: partial call feature
type: Ontology Class
---

# partial call feature

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialCallFeature>

## Definition

call feature whereby the issuer can recall part of the issue on scheduled dates, where bonds are selected to be called according to some rule, or by selecting various bonds at random

## Relationships

- **Subclass of**: [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)

## Constraints

- **[hasPartialRedemptionAllocationConvention](/concepts/fibo/SEC/Debt/Bonds/hasPartialRedemptionAllocationConvention.md)**: some values from of type [PartialRedemptionAllocationConvention](/concepts/fibo/SEC/Debt/Bonds/PartialRedemptionAllocationConvention.md)

## Annotations

- **label**: partial call feature
- **definition**: call feature whereby the issuer can recall part of the issue on scheduled dates, where bonds are selected to be called according to some rule, or by selecting various bonds at random

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
