---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: voting right
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual right that specifies shareholder voting entitlements, such as to elect directors, elect outside auditors,
      and vote on matters of corporate policy
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Voting may involve decisions on issuing securities, initiating stock splits, and making substantial changes in
      the corporation's operations. Note that a given share may not have voting rights, in which case the number of votes
      per share would be zero.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/ContractualRight.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualRight
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/VotingRight
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: voting right
type: Ontology Class
---

# voting right

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/VotingRight>

## Definition

contractual right that specifies shareholder voting entitlements, such as to elect directors, elect outside auditors, and vote on matters of corporate policy

## Relationships

- **Subclass of**: [ContractualRight](/concepts/fibo/FND/Law/LegalCapacity/ContractualRight.md)

## Constraints

- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from of type [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Annotations

- **label**: voting right
- **definition**: contractual right that specifies shareholder voting entitlements, such as to elect directors, elect outside auditors, and vote on matters of corporate policy
- **explanatoryNote**: Voting may involve decisions on issuing securities, initiating stock splits, and making substantial changes in the corporation's operations. Note that a given share may not have voting rights, in which case the number of votes per share would be zero.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
