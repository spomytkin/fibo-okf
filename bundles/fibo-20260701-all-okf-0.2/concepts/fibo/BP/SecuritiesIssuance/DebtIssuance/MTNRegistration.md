---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: m t n registration
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteIssuanceProgramme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/Registration.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Registration
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/MTNRegistration
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: m t n registration
type: Ontology Class
---

# m t n registration

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/MTNRegistration>

## Relationships

- **Subclass of**: [Registration](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/Registration.md)

## Constraints

- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [MediumTermNoteIssuanceProgramme](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteIssuanceProgramme.md)

## Annotations

- **label** (en): m t n registration

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
