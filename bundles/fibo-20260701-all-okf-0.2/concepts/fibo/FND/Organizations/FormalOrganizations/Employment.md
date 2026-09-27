---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: situation representing the state of being employed, i.e., the relationship that holds between an employer and employee
      for some period of time
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: This definition does not include workers in contingent arrangements, such as independent contractors, leased employees,
      temporary employees, on-call workers, and others that do not have a direct contractual relationship with the employer.
      The distinction is important for legal reasons, particularly for regulatory reporting with respect to responsible parties
      such as corporate officers, lending officers, others authorized or licensed to perform certain tasks, and traders, for
      example.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the broadest sense, employment is the situation in which someone is fully engaged in doing something that they
      want to do. From a FIBO perspective, however, employment is understood to be more specific. It is the relationship between
      two parties, evidenced by an implicit or explicit contract, in which work is compensated and in which one party, a legal
      person, typically a formal organization, acts as the employer and the other, typically a legally capable natural person,
      as the employee.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/hasEmployedParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/hasEmployingParty
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/Membership
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employment
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: employment
type: Ontology Class
---

# employment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employment>

## Definition

situation representing the state of being employed, i.e., the relationship that holds between an employer and employee for some period of time

## Relationships

- **Subclass of**: [Membership](<https://www.omg.org/spec/Commons/Organizations/Membership>)

## Constraints

- **[hasEmployedParty](/concepts/fibo/FND/Organizations/FormalOrganizations/hasEmployedParty.md)**: some values from of type [Employee](/concepts/fibo/FND/Organizations/FormalOrganizations/Employee.md)
- **[hasEmployingParty](/concepts/fibo/FND/Organizations/FormalOrganizations/hasEmployingParty.md)**: some values from of type [Employer](/concepts/fibo/FND/Organizations/FormalOrganizations/Employer.md)

## Annotations

- **label** (en): employment
- **definition**: situation representing the state of being employed, i.e., the relationship that holds between an employer and employee for some period of time
- **scopeNote**: This definition does not include workers in contingent arrangements, such as independent contractors, leased employees, temporary employees, on-call workers, and others that do not have a direct contractual relationship with the employer. The distinction is important for legal reasons, particularly for regulatory reporting with respect to responsible parties such as corporate officers, lending officers, others authorized or licensed to perform certain tasks, and traders, for example.
- **explanatoryNote**: In the broadest sense, employment is the situation in which someone is fully engaged in doing something that they want to do. From a FIBO perspective, however, employment is understood to be more specific. It is the relationship between two parties, evidenced by an implicit or explicit contract, in which work is compensated and in which one party, a legal person, typically a formal organization, acts as the employer and the other, typically a legally capable natural person, as the employee.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
