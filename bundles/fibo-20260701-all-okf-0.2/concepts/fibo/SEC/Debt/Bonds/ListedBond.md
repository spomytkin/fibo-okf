---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: listed bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond that may be traded on an exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Most exchange traded bonds are corporate bonds (but most corporate bonds are not exchange traded bonds).
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/UnlistedBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UnlistedBond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ListedBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: listed bond
type: Ontology Class
---

# listed bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ListedBond>

## Definition

bond that may be traded on an exchange

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)
- **Subclass of**: [ListedSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md)

## Constraints

- **Disjoint with**: [UnlistedBond](/concepts/fibo/SEC/Debt/Bonds/UnlistedBond.md)

## Annotations

- **label**: listed bond
- **definition**: bond that may be traded on an exchange
- **explanatoryNote**: Most exchange traded bonds are corporate bonds (but most corporate bonds are not exchange traded bonds).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
