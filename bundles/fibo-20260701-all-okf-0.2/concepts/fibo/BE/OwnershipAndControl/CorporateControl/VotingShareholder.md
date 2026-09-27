---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: voting shareholder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: shareholder whose shares confer the right to vote in corporate elections, including the right to elect directors
      at annual or special meetings, and to express their views to corporate management and directors on significant issues
      that may affect the value of those shares
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A voting shareholder may exercise control over board composition by (1) attending a shareholder meeting and voting
      directly, (2) assigning a proxy to vote on their behalf, either as specified in the recommendations made in the proxy
      card or as indicated in a manner that deviates from those recommendations but is detailed on the proxy card, (3) by
      rejection of the proxy, either implicitly or explicitly, or (4) through a direct ballot that they create themselves.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/elects
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholder
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/VotingShareholder
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: voting shareholder
type: Ontology Class
---

# voting shareholder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/VotingShareholder>

## Definition

shareholder whose shares confer the right to vote in corporate elections, including the right to elect directors at annual or special meetings, and to express their views to corporate management and directors on significant issues that may affect the value of those shares

## Relationships

- **Subclass of**: [DeJureControllingInterestParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)
- **Subclass of**: [Shareholder](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md)

## Constraints

- **[elects](/concepts/fibo/BE/OwnershipAndControl/Executives/elects.md)**: min qualified cardinality 0 of type [BoardMember](/concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md)

## Annotations

- **label**: voting shareholder
- **definition**: shareholder whose shares confer the right to vote in corporate elections, including the right to elect directors at annual or special meetings, and to express their views to corporate management and directors on significant issues that may affect the value of those shares
- **explanatoryNote**: A voting shareholder may exercise control over board composition by (1) attending a shareholder meeting and voting directly, (2) assigning a proxy to vote on their behalf, either as specified in the recommendations made in the proxy card or as indicated in a manner that deviates from those recommendations but is detailed on the proxy card, (3) by rejection of the proxy, either implicitly or explicitly, or (4) through a direct ballot that they create themselves.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
