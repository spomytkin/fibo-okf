---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: implicit full faith credit bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond issued by a government sponsored agency or corporation rather than by the government directly
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: It doesn't carry an explicit full faith and credit guarantee but the market believes the government wouldn't let
      it default or fail.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: implicit full faith and credit bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/UnsecuredBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UnsecuredBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ImplicitFullFaithCreditBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: implicit full faith credit bond
type: Ontology Class
---

# implicit full faith credit bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ImplicitFullFaithCreditBond>

## Definition

bond issued by a government sponsored agency or corporation rather than by the government directly

## Relationships

- **Subclass of**: [UnsecuredBond](/concepts/fibo/SEC/Debt/Bonds/UnsecuredBond.md)

## Annotations

- **label**: implicit full faith credit bond
- **definition**: bond issued by a government sponsored agency or corporation rather than by the government directly
- **explanatoryNote**: It doesn't carry an explicit full faith and credit guarantee but the market believes the government wouldn't let it default or fail.
- **synonym**: implicit full faith and credit bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
