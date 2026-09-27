---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: filing for bankruptcy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit event that involves a request to a court to be recognized as bankrupt
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The bankruptcy process is initiated via a petition filed by the debtor or on behalf of creditors. The debtor's
      assets may be used to repay a portion of outstanding debt as specified by the court or a court-appointed individual.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/FilingForBankruptcy
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: filing for bankruptcy
type: Ontology Class
---

# filing for bankruptcy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/FilingForBankruptcy>

## Definition

credit event that involves a request to a court to be recognized as bankrupt

## Relationships

- **Subclass of**: [EntitySpecificCreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent.md)

## Annotations

- **label** (en): filing for bankruptcy
- **definition** (en): credit event that involves a request to a court to be recognized as bankrupt
- **explanatoryNote** (en): The bankruptcy process is initiated via a petition filed by the debtor or on behalf of creditors. The debtor's assets may be used to repay a portion of outstanding debt as specified by the court or a court-appointed individual.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
