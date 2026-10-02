---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commitment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: promise made by some party to act or refrain from acting in some manner
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such a promise often results a corresponding right or obligation with respect to another party to the commitment.
      Thus, obligations and rights are considered as reciprocal aspects of a commitment.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: commitment
type: Ontology Class
---

# commitment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment>

## Definition

promise made by some party to act or refrain from acting in some manner

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label** (en): commitment
- **definition**: promise made by some party to act or refrain from acting in some manner
- **explanatoryNote**: Such a promise often results a corresponding right or obligation with respect to another party to the commitment. Thus, obligations and rights are considered as reciprocal aspects of a commitment.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
