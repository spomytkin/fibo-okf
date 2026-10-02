---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: negotiated understanding between two or more parties, reflecting the offer and acceptance of commitments on the
      part of either party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: All agreements are time bound, whether implicit or explicitly stated, and thus an agreement reflects a state of
      affairs that holds for some period of time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
  - cardinality: 2
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: agreement
type: Ontology Class
---

# agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement>

## Definition

negotiated understanding between two or more parties, reflecting the offer and acceptance of commitments on the part of either party

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[confers](/concepts/fibo/FND/Relations/Relations/confers.md)**: min qualified cardinality 0 of type [Commitment](/concepts/fibo/FND/Agreements/Agreements/Commitment.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: min qualified cardinality 2 of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label** (en): agreement
- **definition**: negotiated understanding between two or more parties, reflecting the offer and acceptance of commitments on the part of either party
- **explanatoryNote**: All agreements are time bound, whether implicit or explicitly stated, and thus an agreement reflects a state of affairs that holds for some period of time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
