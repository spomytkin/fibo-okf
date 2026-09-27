---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bullet bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond whose entire principal value is paid on the maturity date, rather than amortized over its lifetime
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/AmortizingBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/AmortizingBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/CallableBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableBond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BulletPrincipalRepaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRepaymentTerms
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BulletBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bullet bond
type: Ontology Class
---

# bullet bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BulletBond>

## Definition

bond whose entire principal value is paid on the maturity date, rather than amortized over its lifetime

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Constraints

- **Disjoint with**: [AmortizingBond](/concepts/fibo/SEC/Debt/Bonds/AmortizingBond.md)
- **Disjoint with**: [CallableBond](/concepts/fibo/SEC/Debt/Bonds/CallableBond.md)
- **[hasRepaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasRepaymentTerms.md)**: some values from of type [BulletPrincipalRepaymentTerms](/concepts/fibo/SEC/Debt/Bonds/BulletPrincipalRepaymentTerms.md)

## Annotations

- **label**: bullet bond
- **definition**: bond whose entire principal value is paid on the maturity date, rather than amortized over its lifetime

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
