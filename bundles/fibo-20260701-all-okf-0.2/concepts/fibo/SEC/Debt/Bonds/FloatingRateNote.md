---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: floating rate note
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond with a variable interest rate based on a published reference interest rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The adjustments to the interest rate (coupon) are made periodically, usually on a quarterly or monthly basis, and
      are tied to a certain money-market index. Also known as a "floater". For example six months USD LIBOR + 0.20%.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariableCouponBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FloatingRateNote
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: floating rate note
type: Ontology Class
---

# floating rate note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FloatingRateNote>

## Definition

bond with a variable interest rate based on a published reference interest rate

## Relationships

- **Subclass of**: [VariableCouponBond](/concepts/fibo/SEC/Debt/Bonds/VariableCouponBond.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: some values from of type [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)

## Annotations

- **label**: floating rate note
- **definition**: bond with a variable interest rate based on a published reference interest rate
- **explanatoryNote**: The adjustments to the interest rate (coupon) are made periodically, usually on a quarterly or monthly basis, and are tied to a certain money-market index. Also known as a "floater". For example six months USD LIBOR + 0.20%.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
