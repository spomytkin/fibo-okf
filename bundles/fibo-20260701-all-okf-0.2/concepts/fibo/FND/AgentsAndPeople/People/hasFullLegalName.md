---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has full legal name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the complete name of a person, typically used in formal situations including those of a legal or contractual
      nature
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/hasPersonName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasPersonName
  - concept: /concepts/fibo/FND/Relations/Relations/hasLegalName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasFullLegalName
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has full legal name
type: Ontology Property
---

# has full legal name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasFullLegalName>

## Definition

indicates the complete name of a person, typically used in formal situations including those of a legal or contractual nature

## Relationships

- **Subproperty of**: [hasPersonName](/concepts/fibo/FND/AgentsAndPeople/People/hasPersonName.md)
- **Subproperty of**: [hasLegalName](/concepts/fibo/FND/Relations/Relations/hasLegalName.md)

## Annotations

- **label**: has full legal name
- **definition**: indicates the complete name of a person, typically used in formal situations including those of a legal or contractual nature

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
