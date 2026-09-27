---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency m b s pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A pool investment consisting of a collection of Agency MBS instruments.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This pool may be used as the underlying for an agency CMO. Non agency CMOs do not exist.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MBSPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MBSPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMBSPool
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: agency m b s pool
type: Ontology Class
---

# agency m b s pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMBSPool>

## Definition

A pool investment consisting of a collection of Agency MBS instruments.

## Relationships

- **Subclass of**: [MBSPool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MBSPool.md)

## Annotations

- **label** (en): agency m b s pool
- **definition** (en): A pool investment consisting of a collection of Agency MBS instruments.
- **explanatoryNote** (en): This pool may be used as the underlying for an agency CMO. Non agency CMOs do not exist.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
