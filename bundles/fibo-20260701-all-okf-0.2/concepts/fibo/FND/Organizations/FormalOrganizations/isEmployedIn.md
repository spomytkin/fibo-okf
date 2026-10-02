---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is employed in
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the context of employment in which someone is employed
  domain:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
  range:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employment
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/isOrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployedIn
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: is employed in
type: Ontology Property
---

# is employed in

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployedIn>

## Definition

indicates the context of employment in which someone is employed

## Relationships

- **Domain**: [Employee](/concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md)
- **Range**: [Employment](/concepts/fibo/FND/Organizations/FormalOrganizations/Employment.md)
- **Subproperty of**: [isOrganizationMember](<https://www.omg.org/spec/Commons/Organizations/isOrganizationMember>)

## Annotations

- **label**: is employed in
- **definition**: indicates the context of employment in which someone is employed

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
