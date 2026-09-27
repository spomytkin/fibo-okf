---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan purpose
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A selection of different types of loan purpose, being the purpose for which and manner in which loan (credit) draw-down
      amounts are to be used. This shows the purpose for which credit is to be used, and implies certain kinds of fact that
      relate to that specific type of loan e.g. mortgages. These are also identified as tranche types in tranches of a credit
      facility.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/Objective.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Objective
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanPurpose
sources:
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: loan purpose
type: Ontology Class
---

# loan purpose

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanPurpose>

## Definition

A selection of different types of loan purpose, being the purpose for which and manner in which loan (credit) draw-down amounts are to be used. This shows the purpose for which credit is to be used, and implies certain kinds of fact that relate to that specific type of loan e.g. mortgages. These are also identified as tranche types in tranches of a credit facility.

## Relationships

- **Subclass of**: [Objective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/Objective.md)

## Annotations

- **label** (en): loan purpose
- **definition** (en): A selection of different types of loan purpose, being the purpose for which and manner in which loan (credit) draw-down amounts are to be used. This shows the purpose for which credit is to be used, and implies certain kinds of fact that relate to that specific type of loan e.g. mortgages. These are also identified as tranche types in tranches of a credit facility.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
