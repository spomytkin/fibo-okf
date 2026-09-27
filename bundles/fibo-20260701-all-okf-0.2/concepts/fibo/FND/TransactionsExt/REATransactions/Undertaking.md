---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: undertaking
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Some undertaking to act.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This could be an undertaking to deliver something, to do something and so on. These correspond to negative and
      positive pledges in the contract.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentRight
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/bestows
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/givesRiseTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/isMadeAsPartOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentObligation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/isUndertakingTo
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/Undertaking
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: undertaking
type: Ontology Class
---

# undertaking

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/Undertaking>

## Definition

Some undertaking to act.

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)
- **[bestows](/concepts/fibo/FND/TransactionsExt/REATransactions/bestows.md)**: some values from of type [ContingentRight](/concepts/fibo/FND/Law/LegalCapacity/ContingentRight.md)
- **[givesRiseTo](/concepts/fibo/FND/TransactionsExt/REATransactions/givesRiseTo.md)**: some values from of type [Commitment](/concepts/fibo/FND/Agreements/Agreements/Commitment.md)
- **[isMadeAsPartOf](/concepts/fibo/FND/TransactionsExt/REATransactions/isMadeAsPartOf.md)**: some values from of type [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)
- **[isUndertakingTo](/concepts/fibo/FND/TransactionsExt/REATransactions/isUndertakingTo.md)**: some values from of type [ContingentObligation](/concepts/fibo/FND/Law/LegalCapacity/ContingentObligation.md)

## Annotations

- **label** (en): undertaking
- **definition** (en): Some undertaking to act.
- **explanatoryNote** (en): This could be an undertaking to deliver something, to do something and so on. These correspond to negative and positive pledges in the contract.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
