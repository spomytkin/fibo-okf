---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: multilateral agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: agreements that involve or include multiple parties
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Multilateral agreements are characterized by the participation and commitment of multiple countries or parties
      to achieve a common objective or address a shared issue.
  disjoint_with:
  - concept: /concepts/fibo/FND/Agreements/Agreements/BilateralAgreement.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/BilateralAgreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 3
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Agreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/MultilateralAgreement
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: multilateral agreement
type: Ontology Class
---

# multilateral agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/MultilateralAgreement>

## Definition

agreements that involve or include multiple parties

## Relationships

- **Subclass of**: [Agreement](/concepts/fibo/FND/Agreements/Agreements/Agreement.md)

## Constraints

- **Disjoint with**: [BilateralAgreement](/concepts/fibo/FND/Agreements/Agreements/BilateralAgreement.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: min qualified cardinality 3 of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label** (en): multilateral agreement
- **definition**: agreements that involve or include multiple parties
- **explanatoryNote**: Multilateral agreements are characterized by the participation and commitment of multiple countries or parties to achieve a common objective or address a shared issue.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
