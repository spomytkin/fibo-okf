---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: brokerage account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account offered by a broker that allows the investor to deposit funds and place investment orders
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The investor owns the assets contained in the brokerage account and must usually claim as income any capital gains
      incurred.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
    value: Nc5fbe9348e744618ba270809fb685cde
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentAccount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BrokerageAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: brokerage account
type: Ontology Class
---

# brokerage account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/BrokerageAccount>

## Definition

account offered by a broker that allows the investor to deposit funds and place investment orders

## Relationships

- **Subclass of**: [InvestmentAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentAccount.md)

## Constraints

- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from value `Nc5fbe9348e744618ba270809fb685cde`

## Annotations

- **label**: brokerage account
- **definition**: account offered by a broker that allows the investor to deposit funds and place investment orders
- **explanatoryNote**: The investor owns the assets contained in the brokerage account and must usually claim as income any capital gains incurred.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
