---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has age of majority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates someone to the age required to attain the capacity to engage in certain transactions or be treated legally
      as an adult in some jurisdiction
  range:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/AgeOfMajority.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/AgeOfMajority
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAge.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAge
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasAgeOfMajority
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has age of majority
type: Ontology Property
---

# has age of majority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasAgeOfMajority>

## Definition

relates someone to the age required to attain the capacity to engage in certain transactions or be treated legally as an adult in some jurisdiction

## Relationships

- **Range**: [AgeOfMajority](/concepts/fibo/FND/AgentsAndPeople/People/AgeOfMajority.md)
- **Subproperty of**: [hasAge](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAge.md)

## Annotations

- **label**: has age of majority
- **definition**: relates someone to the age required to attain the capacity to engage in certain transactions or be treated legally as an adult in some jurisdiction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
