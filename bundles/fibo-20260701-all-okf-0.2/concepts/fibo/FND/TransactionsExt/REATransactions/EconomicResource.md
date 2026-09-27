---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: economic resource
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Anything that can bought sold or exchanged.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Formerly labeled as Negotiable Thing. Changed to REA terminology with no effect on meaning. Note that this is
      a relative thing - the thing which is itself the economic resource, is some good or some service (i.e. some physical
      thing or some event/activity) which can be framed as an economic resource in the context of exchanging it for some other
      economic resource. Scope Note: Economic Resource may also define things which are not exchanged but are defined as resources
      in some other context, for example Capital is a kind of economic resource.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicTransaction
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/definedInContextOf
  - filler: http://www.w3.org/2002/07/owl#Thing
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/takesMaterialForm
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicResource
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: economic resource
type: Ontology Class
---

# economic resource

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicResource>

## Definition

Anything that can bought sold or exchanged.

## Constraints

- **[definedInContextOf](/concepts/fibo/FND/TransactionsExt/REATransactions/definedInContextOf.md)**: some values from of type [EconomicTransaction](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md)
- **[takesMaterialForm](/concepts/fibo/FND/TransactionsExt/REATransactions/takesMaterialForm.md)**: some values from of type [Thing](<http://www.w3.org/2002/07/owl#Thing>)

## Annotations

- **label** (en): economic resource
- **definition** (en): Anything that can bought sold or exchanged.
- **editorialNote** (en): Formerly labeled as Negotiable Thing. Changed to REA terminology with no effect on meaning. Note that this is a relative thing - the thing which is itself the economic resource, is some good or some service (i.e. some physical thing or some event/activity) which can be framed as an economic resource in the context of exchanging it for some other economic resource. Scope Note: Economic Resource may also define things which are not exchanged but are defined as resources in some other context, for example Capital is a kind of economic resource.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
