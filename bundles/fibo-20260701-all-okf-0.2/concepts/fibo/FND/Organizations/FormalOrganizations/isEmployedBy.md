---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is employed by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the party (legal person or formal organization) that employs someone
  domain:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/Person.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/experiencesDirectly
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployedBy
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: is employed by
type: Ontology Property
---

# is employed by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployedBy>

## Definition

indicates the party (legal person or formal organization) that employs someone

## Relationships

- **Domain**: [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **Range**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **Subproperty of**: [experiencesDirectly](<https://www.omg.org/spec/Commons/PartiesAndSituations/experiencesDirectly>)

## Annotations

- **label**: is employed by
- **definition**: indicates the party (legal person or formal organization) that employs someone

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
