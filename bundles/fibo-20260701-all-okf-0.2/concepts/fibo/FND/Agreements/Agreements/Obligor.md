---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: obligor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that is bound legally or by agreement to repay a debt, make a payment, do something, or refrain from doing
      something
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: obligated party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: obligator
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/hasObligation
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N94a14512d83343389a05d1d96cf26caa
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligor
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: obligor
type: Ontology Class
---

# obligor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligor>

## Definition

party that is bound legally or by agreement to repay a debt, make a payment, do something, or refrain from doing something

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[hasObligation](/concepts/fibo/FND/Agreements/Agreements/hasObligation.md)**: some values from of type [Commitment](/concepts/fibo/FND/Agreements/Agreements/Commitment.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N94a14512d83343389a05d1d96cf26caa`

## Annotations

- **label**: obligor
- **definition**: party that is bound legally or by agreement to repay a debt, make a payment, do something, or refrain from doing something
- **synonym**: obligated party
- **synonym**: obligator

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
