---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: strip bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond that is part of a series of bonds formed by selling each interest payment and the principal amount of a bond
      as separate zero coupon bonds.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/ZeroCouponBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponBond
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/Strip.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/Strip
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/StripBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: strip bond
type: Ontology Class
---

# strip bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/StripBond>

## Definition

bond that is part of a series of bonds formed by selling each interest payment and the principal amount of a bond as separate zero coupon bonds.

## Relationships

- **Subclass of**: [ZeroCouponBond](/concepts/fibo/SEC/Debt/Bonds/ZeroCouponBond.md)
- **Subclass of**: [Strip](/concepts/fibo/SEC/Debt/DebtInstruments/Strip.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Annotations

- **label**: strip bond
- **definition**: bond that is part of a series of bonds formed by selling each interest payment and the principal amount of a bond as separate zero coupon bonds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
