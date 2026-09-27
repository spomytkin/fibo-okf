---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity linked bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond based on the return on an equity over time, i.e. the price and dividend payments or the total return (similar
      to total return swaps)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariableCouponBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/EquityLinkedBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: equity linked bond
type: Ontology Class
---

# equity linked bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/EquityLinkedBond>

## Definition

bond based on the return on an equity over time, i.e. the price and dividend payments or the total return (similar to total return swaps)

## Relationships

- **Subclass of**: [VariableCouponBond](/concepts/fibo/SEC/Debt/Bonds/VariableCouponBond.md)

## Annotations

- **label**: equity linked bond
- **definition**: bond based on the return on an equity over time, i.e. the price and dividend payments or the total return (similar to total return swaps)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
