---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: owns
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates something that a party holds title to and may possess
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/playsActiveRoleThatDirectlyAffects
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/owns
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: owns
type: Ontology Property
---

# owns

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/owns>

## Definition

indicates something that a party holds title to and may possess

## Relationships

- **Domain**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Subproperty of**: [playsActiveRoleThatDirectlyAffects](<https://www.omg.org/spec/Commons/PartiesAndSituations/playsActiveRoleThatDirectlyAffects>)

## Annotations

- **label**: owns
- **definition**: indicates something that a party holds title to and may possess

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
