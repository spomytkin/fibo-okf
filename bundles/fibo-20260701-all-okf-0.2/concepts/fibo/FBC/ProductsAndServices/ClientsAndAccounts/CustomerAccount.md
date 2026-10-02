---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: customer account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account that represents an identified, named collection of balances and cumulative totals used to summarize customer
      transaction-related activity over a designated period of time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: financial service account
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
    value: Nf7eaef0daac54a4e9861794dde3390f5
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
    value: N8ae9a3dffa54443c8019820bf3b89287
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: customer account
type: Ontology Class
---

# customer account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount>

## Definition

account that represents an identified, named collection of balances and cumulative totals used to summarize customer transaction-related activity over a designated period of time

## Relationships

- **Subclass of**: [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Constraints

- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: some values from value `Nf7eaef0daac54a4e9861794dde3390f5`
- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: some values from of type [CustomerAccountHolder](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [ServiceAgreement](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: some values from of type [AccountIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from value `N8ae9a3dffa54443c8019820bf3b89287`

## Annotations

- **label**: customer account
- **definition**: account that represents an identified, named collection of balances and cumulative totals used to summarize customer transaction-related activity over a designated period of time
- **synonym**: financial service account

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
