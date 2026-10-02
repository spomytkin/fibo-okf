---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market transaction payment terms
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/EconomicContractTermsSet.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicContractTermsSet
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms
sources:
- id: fibo-source-c6db657dd3
  resource: references/fibo/FND/TransactionsExt/MarketTransactions.rdf
  sha256: c6db657dd322bad9135c79dfe7fe0e80f7e2c5aaff92ca4b48c056a156ccc943
  title: FIBO source FND/TransactionsExt/MarketTransactions.rdf
title: market transaction payment terms
type: Ontology Class
---

# market transaction payment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms>

## Relationships

- **Subclass of**: [EconomicContractTermsSet](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicContractTermsSet.md)

## Constraints

- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [Payment](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md)

## Annotations

- **label** (en): market transaction payment terms

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
