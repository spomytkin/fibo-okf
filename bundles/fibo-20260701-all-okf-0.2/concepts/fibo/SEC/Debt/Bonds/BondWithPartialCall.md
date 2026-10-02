---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond with partial call
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond with a feature whereby the issue can be partially called for amounts that are at the discretion of the issuer
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/PartialCallFeature
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasCallFeature
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/CallableBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondWithPartialCall
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond with partial call
type: Ontology Class
---

# bond with partial call

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondWithPartialCall>

## Definition

bond with a feature whereby the issue can be partially called for amounts that are at the discretion of the issuer

## Relationships

- **Subclass of**: [CallableBond](/concepts/fibo/SEC/Debt/Bonds/CallableBond.md)

## Constraints

- **[hasCallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/hasCallFeature.md)**: some values from of type [PartialCallFeature](/concepts/fibo/SEC/Debt/Bonds/PartialCallFeature.md)

## Annotations

- **label**: bond with partial call
- **definition**: bond with a feature whereby the issue can be partially called for amounts that are at the discretion of the issuer

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
