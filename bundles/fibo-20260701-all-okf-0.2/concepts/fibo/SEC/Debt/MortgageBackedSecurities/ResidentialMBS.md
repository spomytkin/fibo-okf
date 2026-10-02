---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: residential m b s
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Residential Mortgage-Backed Securities, which are trust certificates (bonds) backed by a pool of residential mortgage
      loans.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Notes from CESR: They are issued by banks and backed by an underlying pool of residential mortgages. There can
      be some distinctions between prime RMBS and sub-prime/non-conforming RMBS although there is no consensus about what
      constitutes a sub-prime/non-conforming mortgage in Europe.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/ResidentialMBS
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: residential m b s
type: Ontology Class
---

# residential m b s

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/ResidentialMBS>

## Definition

Residential Mortgage-Backed Securities, which are trust certificates (bonds) backed by a pool of residential mortgage loans.

## Relationships

- **Subclass of**: [MortgageBackedSecurity](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md)

## Annotations

- **label** (en): residential m b s
- **definition** (en): Residential Mortgage-Backed Securities, which are trust certificates (bonds) backed by a pool of residential mortgage loans.
- **explanatoryNote** (en): Notes from CESR: They are issued by banks and backed by an underlying pool of residential mortgages. There can be some distinctions between prime RMBS and sub-prime/non-conforming RMBS although there is no consensus about what constitutes a sub-prime/non-conforming mortgage in Europe.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
