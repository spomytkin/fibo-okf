---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: obligee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party to whom some commitment or obligation is owed, either legally or per the terms of an agreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N58ae52d4abed487ea6fafcd6b218f313
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligee
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: obligee
type: Ontology Class
---

# obligee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligee>

## Definition

party to whom some commitment or obligation is owed, either legally or per the terms of an agreement

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N58ae52d4abed487ea6fafcd6b218f313`

## Annotations

- **label**: obligee
- **definition**: party to whom some commitment or obligation is owed, either legally or per the terms of an agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
