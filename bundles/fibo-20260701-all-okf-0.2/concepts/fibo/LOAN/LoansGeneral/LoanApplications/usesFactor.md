---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: uses factor
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates e.g. a risk assessment to something used as a factor to make the assessment
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There is intentionally no range for this property, so as not to limit what can be used as a factor. Often it will
      be a measure such as borrower monthly income. Thus, having a class called Factor seems unhelpful.
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/usesFactor
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: uses factor
type: Ontology Property
---

# uses factor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/usesFactor>

## Definition

relates e.g. a risk assessment to something used as a factor to make the assessment

## Relationships

- **Subproperty of**: [isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)

## Annotations

- **label** (en): uses factor
- **definition** (en): relates e.g. a risk assessment to something used as a factor to make the assessment
- **explanatoryNote**: There is intentionally no range for this property, so as not to limit what can be used as a factor. Often it will be a measure such as borrower monthly income. Thus, having a class called Factor seems unhelpful.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
