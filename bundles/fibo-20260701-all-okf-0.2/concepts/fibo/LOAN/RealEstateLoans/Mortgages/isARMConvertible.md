---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is ARM convertible
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether or not the loan can be converted into an adjustable-rate mortgage contract (ARM)
  domain:
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/isARMConvertible
sources:
- id: fibo-source-69fec2eeb0
  resource: references/fibo/LOAN/RealEstateLoans/Mortgages.rdf
  sha256: 69fec2eeb0f7fc099e11c13a9ed3e6b5a1902c2f2a2af30a81282d1f4a6bdfa5
  title: FIBO source LOAN/RealEstateLoans/Mortgages.rdf
title: is ARM convertible
type: Ontology Property
---

# is ARM convertible

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/isARMConvertible>

## Definition

indicates whether or not the loan can be converted into an adjustable-rate mortgage contract (ARM)

## Relationships

- **Domain**: [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is ARM convertible
- **definition** (en): indicates whether or not the loan can be converted into an adjustable-rate mortgage contract (ARM)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
