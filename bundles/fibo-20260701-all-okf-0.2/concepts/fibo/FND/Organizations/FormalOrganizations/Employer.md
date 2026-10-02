---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that provides compensation, including wages or a salary and potentially other benefits, in exchange for work
      performed by one or more people, and that has the right to control and direct the employee in the material details of
      how the work is to be performed
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/hasEmployee
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employment
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/isEmployingParty
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/MemberBearingOrganization
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employer
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: employer
type: Ontology Class
---

# employer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employer>

## Definition

party that provides compensation, including wages or a salary and potentially other benefits, in exchange for work performed by one or more people, and that has the right to control and direct the employee in the material details of how the work is to be performed

## Relationships

- **Subclass of**: [MemberBearingOrganization](<https://www.omg.org/spec/Commons/Organizations/MemberBearingOrganization>)

## Constraints

- **[hasEmployee](/concepts/fibo/FND/Organizations/FormalOrganizations/hasEmployee.md)**: some values from of type [Employee](/concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md)
- **[isEmployingParty](/concepts/fibo/FND/Organizations/FormalOrganizations/isEmployingParty.md)**: some values from of type [Employment](/concepts/fibo/FND/Organizations/FormalOrganizations/Employment.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Annotations

- **label**: employer
- **definition**: party that provides compensation, including wages or a salary and potentially other benefits, in exchange for work performed by one or more people, and that has the right to control and direct the employee in the material details of how the work is to be performed

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
