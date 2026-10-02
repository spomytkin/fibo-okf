---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: obligation to pay something, such as an amount of money, good, service, or instrument
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In cases where the debtor and payer are the same legal person, then a debt is equivalent to a payment obligation.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debtor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isOwedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Creditor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isOwedTo
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Commitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: debt
type: Ontology Class
---

# debt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt>

## Definition

obligation to pay something, such as an amount of money, good, service, or instrument

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [Commitment](/concepts/fibo/FND/Agreements/Agreements/Commitment.md)

## Constraints

- **[isOwedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isOwedBy.md)**: some values from of type [Debtor](/concepts/fibo/FBC/DebtAndEquities/Debt/Debtor.md)
- **[isOwedTo](/concepts/fibo/FBC/DebtAndEquities/Debt/isOwedTo.md)**: some values from of type [Creditor](/concepts/fibo/FBC/DebtAndEquities/Debt/Creditor.md)

## Annotations

- **label**: debt
- **definition**: obligation to pay something, such as an amount of money, good, service, or instrument
- **explanatoryNote**: In cases where the debtor and payer are the same legal person, then a debt is equivalent to a payment obligation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
