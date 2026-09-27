---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has unit cost
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an item to its unit cost
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Future consideration: move this property to ProductsAndServices ontology (fibo-fnd-pas-pas).'
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/hasCost.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasCost
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/hasUnitCost
sources:
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: has unit cost
type: Ontology Property
---

# has unit cost

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/hasUnitCost>

## Definition

relates an item to its unit cost

## Relationships

- **Subproperty of**: [hasCost](/concepts/fibo/LOAN/LoansGeneral/Loans/hasCost.md)

## Annotations

- **label**: has unit cost
- **definition**: relates an item to its unit cost
- **editorialNote**: Future consideration: move this property to ProductsAndServices ontology (fibo-fnd-pas-pas).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
