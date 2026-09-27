---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bilateral agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: agreement where two parties commit to perform specific actions or obligations towards each other
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: mutual agreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/BilateralAgreement
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: bilateral agreement
type: Ontology Class
---

# bilateral agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/BilateralAgreement>

## Definition

agreement where two parties commit to perform specific actions or obligations towards each other

## Relationships

- **Subclass of**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)

## Constraints

- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: exact qualified cardinality 2 of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label** (en): bilateral agreement
- **definition**: agreement where two parties commit to perform specific actions or obligations towards each other
- **synonym** (en): mutual agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
