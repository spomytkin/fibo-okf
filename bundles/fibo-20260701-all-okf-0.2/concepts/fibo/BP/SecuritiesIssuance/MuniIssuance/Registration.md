---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registration
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/registeredUnder
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Registration
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: registration
type: Ontology Class
---

# registration

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Registration>

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity.md)

## Constraints

- **[registeredUnder](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/registeredUnder.md)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label** (en): registration

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
