---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has total closing costs
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the total the amount paid at the closing of a real estate transaction, i.e., at the time when the title
      to the property is conveyed (transferred) to the buyer
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Closing costs may be incurred by either the buyer or the seller, and may include fees paid by either or both parties
      for the preparation and recording of documents, title service costs, such as for title search and insurance (typically
      paid by the seller, depending on the jurisdiction), other recording costs, other document or transaction stamps or taxes,
      brokerage commissions, survey, appraisal, inspection and other such fees, home warranties, private mortgage insurance
      (PMI), and so forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/hasCost.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasCost
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasTotalClosingCosts
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has total closing costs
type: Ontology Property
---

# has total closing costs

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasTotalClosingCosts>

## Definition

indicates the total the amount paid at the closing of a real estate transaction, i.e., at the time when the title to the property is conveyed (transferred) to the buyer

## Relationships

- **Subproperty of**: [hasCost](/concepts/fibo/LOAN/LoansGeneral/Loans/hasCost.md)

## Annotations

- **label**: has total closing costs
- **definition**: indicates the total the amount paid at the closing of a real estate transaction, i.e., at the time when the title to the property is conveyed (transferred) to the buyer
- **explanatoryNote**: Closing costs may be incurred by either the buyer or the seller, and may include fees paid by either or both parties for the preparation and recording of documents, title service costs, such as for title search and insurance (typically paid by the seller, depending on the jurisdiction), other recording costs, other document or transaction stamps or taxes, brokerage commissions, survey, appraisal, inspection and other such fees, home warranties, private mortgage insurance (PMI), and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
