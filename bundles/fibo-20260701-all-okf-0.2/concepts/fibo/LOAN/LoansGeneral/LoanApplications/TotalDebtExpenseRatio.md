---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: total debt expense ratio
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ratio of all monthly debt payments of all borrowers, including proposed expenses, with respect to the income of
      the borrowers as relied upon to make a credit decision
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: back end ratio
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: total debt expense ratio
type: Ontology Class
---

# total debt expense ratio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio>

## Definition

ratio of all monthly debt payments of all borrowers, including proposed expenses, with respect to the income of the borrowers as relied upon to make a credit decision

## Relationships

- **Subclass of**: [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Annotations

- **label**: total debt expense ratio
- **definition**: ratio of all monthly debt payments of all borrowers, including proposed expenses, with respect to the income of the borrowers as relied upon to make a credit decision
- **synonym**: back end ratio

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
