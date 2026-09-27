---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency mortgage pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A pool of agency mortgages.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgagePool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgagePool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: agency mortgage pool
type: Ontology Class
---

# agency mortgage pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool>

## Definition

A pool of agency mortgages.

## Relationships

- **Subclass of**: [MortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgagePool.md)

## Constraints

- **Disjoint with**: [NonAgencyMortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool.md)

## Annotations

- **label** (en): agency mortgage pool
- **definition** (en): A pool of agency mortgages.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
