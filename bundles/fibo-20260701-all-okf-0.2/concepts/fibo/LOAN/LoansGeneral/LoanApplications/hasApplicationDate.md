---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has application date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: date on which an application was signed and submitted
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplication.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplication
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Reporting/hasRequestDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/hasRequestDate
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasApplicationDate
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: has application date
type: Ontology Property
---

# has application date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasApplicationDate>

## Definition

date on which an application was signed and submitted

## Relationships

- **Domain**: [LoanApplication](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplication.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasRequestDate](/concepts/fibo/FND/Arrangements/Reporting/hasRequestDate.md)

## Annotations

- **label** (en): has application date
- **definition** (en): date on which an application was signed and submitted

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
