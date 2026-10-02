---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has employed party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the employee in an employment situation
  domain:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employment
  inverse_of:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/isEmployedIn.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployedIn
  range:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/hasOrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/hasEmployedParty
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: has employed party
type: Ontology Property
---

# has employed party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/hasEmployedParty>

## Definition

identifies the employee in an employment situation

## Relationships

- **Domain**: [Employment](/concepts/fibo/FND/Organizations/FormalOrganizations/Employment.md)
- **Inverse of**: [isEmployedIn](/concepts/fibo/FND/Organizations/FormalOrganizations/isEmployedIn.md)
- **Range**: [Employee](/concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md)
- **Subproperty of**: [hasOrganizationMember](<https://www.omg.org/spec/Commons/Organizations/hasOrganizationMember>)

## Annotations

- **label**: has employed party
- **definition**: identifies the employee in an employment situation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
