---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: callable convertible bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: convertible bond that is also callable
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/CallableBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/ConvertibleBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ConvertibleBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableConvertibleBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: callable convertible bond
type: Ontology Class
---

# callable convertible bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableConvertibleBond>

## Definition

convertible bond that is also callable

## Relationships

- **Subclass of**: [CallableBond](/concepts/fibo/SEC/Debt/Bonds/CallableBond.md)
- **Subclass of**: [ConvertibleBond](/concepts/fibo/SEC/Debt/Bonds/ConvertibleBond.md)

## Annotations

- **label**: callable convertible bond
- **definition**: convertible bond that is also callable

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
