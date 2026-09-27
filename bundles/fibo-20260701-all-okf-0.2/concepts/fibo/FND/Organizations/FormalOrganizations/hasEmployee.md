---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has employee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates an employee that is employed by the employer
  domain:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employer
  inverse_of:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/isEmployeeOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployeeOf
  range:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/hasEmployee
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: has employee
type: Ontology Property
---

# has employee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/hasEmployee>

## Definition

indicates an employee that is employed by the employer

## Relationships

- **Domain**: [Employer](/concepts/fibo/FND/Organizations/FormalOrganizations/Employer.md)
- **Inverse of**: [isEmployeeOf](/concepts/fibo/FND/Organizations/FormalOrganizations/isEmployeeOf.md)
- **Range**: [Employee](/concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md)
- **Subproperty of**: [actsOn](<https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn>)

## Annotations

- **label**: has employee
- **definition**: indicates an employee that is employed by the employer

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
