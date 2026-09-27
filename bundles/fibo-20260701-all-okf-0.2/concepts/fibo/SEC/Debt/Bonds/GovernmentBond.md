---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt security issued by a government to fund government spending
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: government-issued bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
  - concept: /concepts/fibo/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: government bond
type: Ontology Class
---

# government bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentBond>

## Definition

debt security issued by a government to fund government spending

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)
- **Subclass of**: [GovernmentIssuedDebtSecurity](/concepts/fibo/SEC/Debt/Bonds/GovernmentIssuedDebtSecurity.md)

## Annotations

- **label**: government bond
- **definition**: debt security issued by a government to fund government spending
- **synonym**: government-issued bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
