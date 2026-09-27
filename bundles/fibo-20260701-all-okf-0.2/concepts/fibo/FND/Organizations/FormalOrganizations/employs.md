---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employs
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates someone that is employed by the legal person
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
  range:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/playsActiveRoleThatDirectlyAffects
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/employs
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: employs
type: Ontology Property
---

# employs

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/employs>

## Definition

indicates someone that is employed by the legal person

## Relationships

- **Domain**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **Range**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **Subproperty of**: [playsActiveRoleThatDirectlyAffects](<https://www.omg.org/spec/Commons/PartiesAndSituations/playsActiveRoleThatDirectlyAffects>)

## Annotations

- **label**: employs
- **definition**: indicates someone that is employed by the legal person

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
