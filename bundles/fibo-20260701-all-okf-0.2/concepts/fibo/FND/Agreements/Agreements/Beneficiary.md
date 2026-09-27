---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: beneficiary
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that receives some benefit or advantage or profits from something
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nf4a9481d48a64adf8f3a90c7889689e2
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Beneficiary
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: beneficiary
type: Ontology Class
---

# beneficiary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Beneficiary>

## Definition

party that receives some benefit or advantage or profits from something

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nf4a9481d48a64adf8f3a90c7889689e2`

## Annotations

- **label**: beneficiary
- **definition**: party that receives some benefit or advantage or profits from something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
