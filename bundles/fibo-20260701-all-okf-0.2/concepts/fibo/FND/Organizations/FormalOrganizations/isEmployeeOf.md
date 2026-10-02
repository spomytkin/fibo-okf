---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is employee of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the formal organization for which the employee works
  domain:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
  range:
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations/Employer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employer
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployeeOf
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: is employee of
type: Ontology Property
---

# is employee of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployeeOf>

## Definition

identifies the formal organization for which the employee works

## Relationships

- **Domain**: [Employee](/concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md)
- **Range**: [Employer](/concepts/fibo/FND/Organizations/FormalOrganizations/Employer.md)
- **Subproperty of**: [isAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy>)

## Annotations

- **label**: is employee of
- **definition**: identifies the formal organization for which the employee works

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
