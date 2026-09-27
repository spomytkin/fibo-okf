---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal age
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: age at which someone acquires the capacity to do something that they were prohibited from doing before under the
      law in some jurisdiction
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/Age.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Age
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/LegalAge
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: legal age
type: Ontology Class
---

# legal age

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/LegalAge>

## Definition

age at which someone acquires the capacity to do something that they were prohibited from doing before under the law in some jurisdiction

## Relationships

- **Subclass of**: [Age](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Age.md)

## Constraints

- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: legal age
- **definition**: age at which someone acquires the capacity to do something that they were prohibited from doing before under the law in some jurisdiction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
