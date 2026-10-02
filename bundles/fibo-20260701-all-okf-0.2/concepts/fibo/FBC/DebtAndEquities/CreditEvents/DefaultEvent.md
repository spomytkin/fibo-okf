---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: default event
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit event representing a failure to meet a contractual obligation, such as failure to repay a debt including
      interest or principal on a loan or security
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A default can occur when a borrower is unable to make timely payments, misses payments, or avoids or stops making
      payments, typically with respect to a single transaction. A default has adverse effects on the borrower's credit and
      ability to borrow in the future, and allows the creditor to demand immediate repayment of the obligation in full.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/BreachOfCovenant
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/DefaultEvent
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: default event
type: Ontology Class
---

# default event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/DefaultEvent>

## Definition

credit event representing a failure to meet a contractual obligation, such as failure to repay a debt including interest or principal on a loan or security

## Relationships

- **Subclass of**: [ObligationSpecificCreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md)

## Constraints

- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: min qualified cardinality 0 of type [BreachOfCovenant](/concepts/fibo/FND/Agreements/Contracts/BreachOfCovenant.md)

## Annotations

- **label** (en): default event
- **definition** (en): credit event representing a failure to meet a contractual obligation, such as failure to repay a debt including interest or principal on a loan or security
- **explanatoryNote** (en): A default can occur when a borrower is unable to make timely payments, misses payments, or avoids or stops making payments, typically with respect to a single transaction. A default has adverse effects on the borrower's credit and ability to borrow in the future, and allows the creditor to demand immediate repayment of the obligation in full.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
