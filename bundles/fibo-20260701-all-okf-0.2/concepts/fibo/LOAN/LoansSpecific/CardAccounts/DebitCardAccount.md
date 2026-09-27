---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debit card account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: card account that is represented by a one or more debit cards
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/DebitCardProduct
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/DebitCard
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isSignifiedBy
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/DebitCardAccount
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: debit card account
type: Ontology Class
---

# debit card account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/DebitCardAccount>

## Definition

card account that is represented by a one or more debit cards

## Relationships

- **Subclass of**: [CardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardAccount.md)

## Constraints

- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: some values from of type [DebitCardProduct](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/DebitCardProduct.md)
- **[isSignifiedBy](<https://www.omg.org/spec/Commons/Designators/isSignifiedBy>)**: some values from of type [DebitCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/DebitCard.md)

## Annotations

- **label**: debit card account
- **definition**: card account that is represented by a one or more debit cards

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
