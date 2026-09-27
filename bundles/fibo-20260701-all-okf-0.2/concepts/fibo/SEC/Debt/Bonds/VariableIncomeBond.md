---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable income bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond whose income may vary over time, because either the coupon rate or principal amount changes in line with an
      index or schedule over the life of the security
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/VariableIncomeSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/VariableIncomeSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableIncomeBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: variable income bond
type: Ontology Class
---

# variable income bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableIncomeBond>

## Definition

bond whose income may vary over time, because either the coupon rate or principal amount changes in line with an index or schedule over the life of the security

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)
- **Subclass of**: [VariableIncomeSecurity](/concepts/fibo/SEC/Debt/DebtInstruments/VariableIncomeSecurity.md)

## Annotations

- **label**: variable income bond
- **definition**: bond whose income may vary over time, because either the coupon rate or principal amount changes in line with an index or schedule over the life of the security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
