---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underwriting process actor
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'any actor within the DTCC Underwriting Process or any other Underwriting Process. Note: At present all these Actors
      (e.g. Underwriter) are defined simply as Process Actors and not as specializations of this type of Actor. Therefore
      this Actor is a Union of all of those.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/UnderwritingProcessActor
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: underwriting process actor
type: Ontology Class
---

# underwriting process actor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/UnderwritingProcessActor>

## Definition

any actor within the DTCC Underwriting Process or any other Underwriting Process. Note: At present all these Actors (e.g. Underwriter) are defined simply as Process Actors and not as specializations of this type of Actor. Therefore this Actor is a Union of all of those.

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Annotations

- **label** (en): underwriting process actor
- **definition** (en): any actor within the DTCC Underwriting Process or any other Underwriting Process. Note: At present all these Actors (e.g. Underwriter) are defined simply as Process Actors and not as specializations of this type of Actor. Therefore this Actor is a Union of all of those.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
