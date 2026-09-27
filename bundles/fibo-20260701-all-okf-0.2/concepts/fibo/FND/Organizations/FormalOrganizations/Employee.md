---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: person in the service of another under any contract of hire, express or implied, oral or written, where the employer
      has the right to control and direct that person in the material details of how the work is to be performed
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployeeOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.bls.gov/opub/mlr/2002/01/art1full.pdf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: employee
type: Ontology Class
---

# employee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee>

## Definition

person in the service of another under any contract of hire, express or implied, oral or written, where the employer has the right to control and direct that person in the material details of how the work is to be performed

## Relationships

- **See also**: [art1full.pdf](<https://www.bls.gov/opub/mlr/2002/01/art1full.pdf>)
- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Constraints

- **[isEmployedIn](/concepts/fibo/FND/Organizations/FormalOrganizations/isEmployedIn.md)**: some values from of type [Employment](/concepts/fibo/FND/Organizations/FormalOrganizations/Employment.md)
- **[isEmployeeOf](/concepts/fibo/FND/Organizations/FormalOrganizations/isEmployeeOf.md)**: some values from of type [Employer](/concepts/fibo/FND/Organizations/FormalOrganizations/Employer.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)

## Annotations

- **label**: employee
- **definition**: person in the service of another under any contract of hire, express or implied, oral or written, where the employer has the right to control and direct that person in the material details of how the work is to be performed

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
