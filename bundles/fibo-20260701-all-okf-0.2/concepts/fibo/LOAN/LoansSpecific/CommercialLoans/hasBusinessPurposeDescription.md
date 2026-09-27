---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has business purpose description
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: provides a description of the purpose of the loan from the perspective of the borrower
  domain:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/CommercialLoan
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Designators/hasDescription
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/hasBusinessPurposeDescription
sources:
- id: fibo-source-c2843be0fa
  resource: references/fibo/LOAN/LoansSpecific/CommercialLoans.rdf
  sha256: c2843be0fac87b4f6ea4a3f88fe40c64784f8800a75ccdb185bbd2265d9bd7c3
  title: FIBO source LOAN/LoansSpecific/CommercialLoans.rdf
title: has business purpose description
type: Ontology Property
---

# has business purpose description

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/hasBusinessPurposeDescription>

## Definition

provides a description of the purpose of the loan from the perspective of the borrower

## Relationships

- **Domain**: [CommercialLoan](/concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md)
- **Subproperty of**: [hasDescription](<https://www.omg.org/spec/Commons/Designators/hasDescription>)

## Annotations

- **label**: has business purpose description
- **definition**: provides a description of the purpose of the loan from the perspective of the borrower

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
