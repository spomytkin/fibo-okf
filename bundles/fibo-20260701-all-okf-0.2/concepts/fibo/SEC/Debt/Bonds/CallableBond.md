---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: callable bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond that includes a stipulation allowing the issuer the right to repurchase and retire the bond at the call price
      after the call protection period
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasExtraordinaryRedemptionProvision
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasCallFeature
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isCallable
    value: 'true'
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: callable bond
type: Ontology Class
---

# callable bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableBond>

## Definition

bond that includes a stipulation allowing the issuer the right to repurchase and retire the bond at the call price after the call protection period

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Constraints

- **[hasExtraordinaryRedemptionProvision](/concepts/fibo/SEC/Debt/Bonds/hasExtraordinaryRedemptionProvision.md)**: max qualified cardinality 1 of type [ExtraordinaryRedemptionProvision](/concepts/fibo/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision.md)
- **[hasCallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/hasCallFeature.md)**: some values from of type [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)
- **[isCallable](/concepts/fibo/SEC/Debt/DebtInstruments/isCallable.md)**: has value value `true`

## Annotations

- **label**: callable bond
- **definition**: bond that includes a stipulation allowing the issuer the right to repurchase and retire the bond at the call price after the call protection period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
