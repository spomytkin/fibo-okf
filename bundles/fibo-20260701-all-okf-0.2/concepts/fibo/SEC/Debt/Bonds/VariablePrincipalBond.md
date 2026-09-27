---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable principal bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond whose principal adjusts over time with changes in an index
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The principal on variable principal bonds adjusts line with an index such as inflation or GDP. For example, for
      a bond linked to the CPI, if inflation rises two percent the principal increases by 2 percent. The coupon rate is typically
      fixed. The best-known example is TIPS or Treasury Inflation Protected Bonds, which are linked to the CPI. TIPs offer
      a real or inflation adjusted rate of return.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableDebtPrincipal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/definesTermsFor
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariableIncomeBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableIncomeBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariablePrincipalBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: variable principal bond
type: Ontology Class
---

# variable principal bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariablePrincipalBond>

## Definition

bond whose principal adjusts over time with changes in an index

## Relationships

- **Subclass of**: [VariableIncomeBond](/concepts/fibo/SEC/Debt/Bonds/VariableIncomeBond.md)

## Constraints

- **[definesTermsFor](/concepts/fibo/FND/Agreements/Contracts/definesTermsFor.md)**: some values from of type [VariableDebtPrincipal](/concepts/fibo/SEC/Debt/Bonds/VariableDebtPrincipal.md)

## Annotations

- **label**: variable principal bond
- **definition**: bond whose principal adjusts over time with changes in an index
- **explanatoryNote**: The principal on variable principal bonds adjusts line with an index such as inflation or GDP. For example, for a bond linked to the CPI, if inflation rises two percent the principal increases by 2 percent. The coupon rate is typically fixed. The best-known example is TIPS or Treasury Inflation Protected Bonds, which are linked to the CPI. TIPs offer a real or inflation adjusted rate of return.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
