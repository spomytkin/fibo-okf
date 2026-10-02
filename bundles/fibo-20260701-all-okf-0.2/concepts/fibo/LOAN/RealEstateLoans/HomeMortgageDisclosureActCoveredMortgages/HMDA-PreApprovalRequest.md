---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: HMDA pre-approval request
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a request for pre-approval of a home purchase loan up to a certain amount, and subject to certain non-credit related
      conditions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: the 2015 Revised HMDA regulation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This request is approved only after a comprehensive analysis of the credit worthiness of the borrower is carried
      out.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-PreApprovalRequest
sources:
- id: fibo-source-c6feed0cf8
  resource: references/fibo/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
  sha256: c6feed0cf8f9c31063c105e293abb9e2add43152d3993dd5c4e7722d89df3473
  title: FIBO source LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
title: HMDA pre-approval request
type: Ontology Class
---

# HMDA pre-approval request

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-PreApprovalRequest>

## Definition

a request for pre-approval of a home purchase loan up to a certain amount, and subject to certain non-credit related conditions

## Relationships

- **Subclass of**: [PreApprovalRequest](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest.md)

## Annotations

- **label**: HMDA pre-approval request
- **definition**: a request for pre-approval of a home purchase loan up to a certain amount, and subject to certain non-credit related conditions
- **adaptedFrom**: the 2015 Revised HMDA regulation.
- **explanatoryNote**: This request is approved only after a comprehensive analysis of the credit worthiness of the borrower is carried out.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
