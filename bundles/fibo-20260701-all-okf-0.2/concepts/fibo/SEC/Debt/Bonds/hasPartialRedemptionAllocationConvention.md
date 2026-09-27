---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has partial redemption allocation convention
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the convention used to determine how the redemption is allocated over the set of bond holders
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/PartialCallFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialCallFeature
  range:
  - concept: /concepts/fibo/SEC/Debt/Bonds/PartialRedemptionAllocationConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialRedemptionAllocationConvention
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasPartialRedemptionAllocationConvention
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has partial redemption allocation convention
type: Ontology Property
---

# has partial redemption allocation convention

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasPartialRedemptionAllocationConvention>

## Definition

indicates the convention used to determine how the redemption is allocated over the set of bond holders

## Relationships

- **Domain**: [PartialCallFeature](/concepts/fibo/SEC/Debt/Bonds/PartialCallFeature.md)
- **Range**: [PartialRedemptionAllocationConvention](/concepts/fibo/SEC/Debt/Bonds/PartialRedemptionAllocationConvention.md)

## Annotations

- **label**: has partial redemption allocation convention
- **definition**: indicates the convention used to determine how the redemption is allocated over the set of bond holders

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
