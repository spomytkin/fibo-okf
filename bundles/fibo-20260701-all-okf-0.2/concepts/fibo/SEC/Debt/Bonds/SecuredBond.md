---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: secured bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond that is backed by collateral, such as a tangible asset or income stream, in addition to a general promise
      to pay
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A secured bond may be collateralized by a claim on real assets, such as a factory or auto fleet; or by a claim
      on a revenue stream. A secured bond differs from a mortgage in that proceeds of the bond sale aren't used to acquire
      the asset.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/UnsecuredBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UnsecuredBond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SecuredBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: secured bond
type: Ontology Class
---

# secured bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SecuredBond>

## Definition

bond that is backed by collateral, such as a tangible asset or income stream, in addition to a general promise to pay

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Constraints

- **Disjoint with**: [UnsecuredBond](/concepts/fibo/SEC/Debt/Bonds/UnsecuredBond.md)

## Annotations

- **label**: secured bond
- **definition**: bond that is backed by collateral, such as a tangible asset or income stream, in addition to a general promise to pay
- **explanatoryNote**: A secured bond may be collateralized by a claim on real assets, such as a factory or auto fleet; or by a claim on a revenue stream. A secured bond differs from a mortgage in that proceeds of the bond sale aren't used to acquire the asset.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
